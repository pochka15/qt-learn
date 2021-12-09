# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionNew_room = QAction(MainWindow)
        self.actionNew_room.setObjectName(u"actionNew_room")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rooms_side_bar = QFrame(self.main_frame)
        self.rooms_side_bar.setObjectName(u"rooms_side_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rooms_side_bar.sizePolicy().hasHeightForWidth())
        self.rooms_side_bar.setSizePolicy(sizePolicy)
        self.rooms_side_bar.setMaximumSize(QSize(500, 16777215))
        self.rooms_side_bar.setStyleSheet(u"")
        self.rooms_side_bar.setFrameShape(QFrame.NoFrame)
        self.rooms_side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.rooms_side_bar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rooms_view = QListView(self.rooms_side_bar)
        self.rooms_view.setObjectName(u"rooms_view")
        self.rooms_view.setStyleSheet(u"border-radius: 20px;")

        self.verticalLayout_5.addWidget(self.rooms_view)


        self.horizontalLayout.addWidget(self.rooms_side_bar)

        self.stacked_widget = QStackedWidget(self.main_frame)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.room_page = QWidget()
        self.room_page.setObjectName(u"room_page")
        self.horizontalLayout_4 = QHBoxLayout(self.room_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.room = QFrame(self.room_page)
        self.room.setObjectName(u"room")
        self.room.setFrameShape(QFrame.NoFrame)
        self.room.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.room)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, 9)
        self.utility_frame = QFrame(self.room)
        self.utility_frame.setObjectName(u"utility_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.utility_frame.sizePolicy().hasHeightForWidth())
        self.utility_frame.setSizePolicy(sizePolicy1)
        self.utility_frame.setLayoutDirection(Qt.LeftToRight)
        self.utility_frame.setFrameShape(QFrame.NoFrame)
        self.utility_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.utility_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.delete_members = QPushButton(self.utility_frame)
        self.delete_members.setObjectName(u"delete_members")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_members.sizePolicy().hasHeightForWidth())
        self.delete_members.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        # endif
        self.delete_members.setPalette(palette)
        self.delete_members.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.delete_members)

        self.add_member = QPushButton(self.utility_frame)
        self.add_member.setObjectName(u"add_member")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        # endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        # endif
        self.add_member.setPalette(palette1)

        self.horizontalLayout_3.addWidget(self.add_member)

        self.verticalLayout_3.addWidget(self.utility_frame, 0, Qt.AlignRight)

        self.room_name = QLabel(self.room)
        self.room_name.setObjectName(u"room_name")
        self.room_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.room_name)

        self.membres_area = QScrollArea(self.room)
        self.membres_area.setObjectName(u"membres_area")
        self.membres_area.setFrameShape(QFrame.NoFrame)
        self.membres_area.setWidgetResizable(True)
        self.members_area_contents = QWidget()
        self.members_area_contents.setObjectName(u"members_area_contents")
        self.members_area_contents.setGeometry(QRect(0, 0, 848, 698))
        self.verticalLayout = QVBoxLayout(self.members_area_contents)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, -1, 9)
        self.members_view = QListView(self.members_area_contents)
        self.members_view.setObjectName(u"members_view")
        self.members_view.setStyleSheet(u"")
        self.members_view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.members_view)

        self.membres_area.setWidget(self.members_area_contents)

        self.verticalLayout_3.addWidget(self.membres_area)

        self.delete_room = QPushButton(self.room)
        self.delete_room.setObjectName(u"delete_room")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        # endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        # endif
        self.delete_room.setPalette(palette2)

        self.verticalLayout_3.addWidget(self.delete_room)

        self.horizontalLayout_4.addWidget(self.room)

        self.stacked_widget.addWidget(self.room_page)
        self.members_page = QWidget()
        self.members_page.setObjectName(u"members_page")
        self.verticalLayout_4 = QVBoxLayout(self.members_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.back_button = QPushButton(self.members_page)
        self.back_button.setObjectName(u"back_button")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        # endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        # endif
        self.back_button.setPalette(palette3)

        self.verticalLayout_4.addWidget(self.back_button, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.members_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.left_spacer = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.left_spacer)

        self.member_input = QLineEdit(self.frame_2)
        self.member_input.setObjectName(u"member_input")
        sizePolicy2.setHeightForWidth(self.member_input.sizePolicy().hasHeightForWidth())
        self.member_input.setSizePolicy(sizePolicy2)
        self.member_input.setMinimumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(14)
        self.member_input.setFont(font)
        self.member_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.member_input)

        self.right_spacer = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.right_spacer)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.dropdown_view = QListView(self.members_page)
        self.dropdown_view.setObjectName(u"dropdown_view")

        self.verticalLayout_4.addWidget(self.dropdown_view)

        self.stacked_widget.addWidget(self.members_page)

        self.horizontalLayout.addWidget(self.stacked_widget)

        self.verticalLayout_2.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        # endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        # endif
        self.menuMenu.setPalette(palette4)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.rooms_view, self.add_member)
        QWidget.setTabOrder(self.add_member, self.delete_members)
        QWidget.setTabOrder(self.delete_members, self.members_view)
        QWidget.setTabOrder(self.members_view, self.delete_room)
        QWidget.setTabOrder(self.delete_room, self.back_button)
        QWidget.setTabOrder(self.back_button, self.member_input)
        QWidget.setTabOrder(self.member_input, self.dropdown_view)
        QWidget.setTabOrder(self.dropdown_view, self.membres_area)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addAction(self.actionNew_room)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+Alt+Q", None))
        #endif // QT_CONFIG(shortcut)
        self.actionNew_room.setText(QCoreApplication.translate("MainWindow", u"New room", None))
#if QT_CONFIG(shortcut)
        self.actionNew_room.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.delete_members.setText(QCoreApplication.translate("MainWindow", u"Delete members", None))
        self.add_member.setText(QCoreApplication.translate("MainWindow", u"Add member", None))
        self.room_name.setText(QCoreApplication.translate("MainWindow", u"Custom room", None))
        self.delete_room.setText(QCoreApplication.translate("MainWindow", u"Delete room", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.member_input.setText("")
        self.member_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Member name...", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

