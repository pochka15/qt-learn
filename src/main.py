import sys
from typing import Optional, List

from PySide2.QtCore import Slot, QModelIndex
from PySide2.QtWidgets import (QApplication, QMainWindow)

from src.global_state import GlobalState
from src.mainwindow import Ui_MainWindow
from src.members_form import MembersForm
from src.room import RoomsModel, MembersModel, create_rooms, RoomDto

global_state = GlobalState()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setup_ui()

        # Models
        self.rooms_model = RoomsModel(create_rooms(global_state.get_next_id))
        self.members_model = MembersModel([])

        # Views
        self.ui.rooms_view.setModel(self.rooms_model)
        self.ui.members_view.setModel(self.members_model)

        self.setup_events()
        self.setup_actions()

        # Children
        self.members_form = MembersForm(self.ui, self.ui_show_room_page, global_state)

    def setup_ui(self):
        self.ui.setupUi(self)
        self.ui_reset_members_view()
        self.ui_show_room_page()

    def setup_actions(self):
        self.ui.actionQuit.triggered.connect(self.exit_app)

    def setup_events(self):
        self.ui.delete_room.clicked.connect(self.delete_selected_room)
        self.ui.delete_members.clicked.connect(self.delete_selected_members)
        self.ui.add_member.clicked.connect(self.ui_show_members_page)

        r_selection = self.ui.rooms_view.selectionModel()
        r_selection.currentChanged.connect(self.handle_room_selection_changed)

        m_selection = self.ui.members_view.selectionModel()
        m_selection.selectionChanged.connect(self.handle_members_selection_changed)

    @Slot()
    def handle_room_selection_changed(self, ind: QModelIndex):
        room: Optional[RoomDto] = ind.data(RoomsModel.DTO_ROLE)
        self.members_model.reset([] if room is None else [member.to_model() for member in room.members])
        self.ui_handle_room_selection_changed(room)

    @Slot()
    def handle_members_selection_changed(self):
        indexes = self.ui.members_view.selectionModel().selectedIndexes()
        self.ui_handle_members_selection_changed(indexes)

    def ui_handle_room_selection_changed(self, room: Optional[RoomDto]):
        if room is None:
            self.ui_reset_members_view()
        else:
            self.ui.room_name.setText(room.name)
            self.ui.delete_room.setVisible(True)

    def ui_reset_members_view(self):
        self.ui.room_name.setText("")
        self.ui.delete_room.setVisible(False)
        self.ui.delete_members.setVisible(False)

    def ui_show_members_page(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.members_page)

    def ui_show_room_page(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.room_page)

    def ui_handle_members_selection_changed(self, indexes: List[QModelIndex]):
        self.ui.delete_members.setVisible(True if len(indexes) > 0 else False)

    @Slot()
    def exit_app(self):
        sys.exit()

    @Slot()
    def delete_selected_room(self):
        selection = self.ui.rooms_view.selectionModel()
        row = selection.currentIndex().row()
        selection.clear()
        self.rooms_model.removeRow(row)

    @Slot()
    def delete_selected_members(self):
        selection = self.ui.members_view.selectionModel()
        indexes = selection.selectedIndexes()
        self.members_model.remove_at_indexes([ind.row() for ind in indexes])
        selection.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
