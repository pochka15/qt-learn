from PySide2.QtCore import QSortFilterProxyModel, Qt, Slot, QModelIndex

from src.global_state import GlobalState
from src.mainwindow import Ui_MainWindow
from src.room import MembersModel, create_random_members, MemberDto


class MembersForm:
    def __init__(self, ui: Ui_MainWindow, on_back_clicked, global_state: GlobalState):
        self.global_state = global_state
        self.on_back_clicked = on_back_clicked
        self.ui = ui

        # Models
        self.members = MembersModel(create_random_members(global_state.get_next_id))
        self.proxy = QSortFilterProxyModel()
        self.setup_proxy()

        # Views
        self.ui.dropdown_view.setModel(self.proxy)

        self.setup_events()

    def setup_events(self):
        self.ui.back_button.clicked.connect(self.handle_back_clicked)
        self.ui.member_input.textChanged.connect(self.proxy.setFilterRegExp)
        selection = self.ui.dropdown_view.selectionModel()
        selection.currentChanged.connect(self.handle_dropdown_selection_changed)

    def setup_proxy(self):
        self.proxy.setSourceModel(self.members)
        self.proxy.setFilterKeyColumn(0)
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)

    @Slot()
    def handle_dropdown_selection_changed(self, ind: QModelIndex):
        # It's a hack, a better way is to think about how to map the index to the index of the source model
        member: MemberDto = self.members.get_first_matching(ind.data())
        # self.members.remove_by_id(member.id)
        # TODO(@pochka15): think about how to update the current model containing members
        print('Todo: Move member: ', member)

    @Slot()
    def handle_back_clicked(self):
        self.on_back_clicked()
