from dataclasses import dataclass
from random import randrange
from typing import List

from PySide2.QtCore import QAbstractListModel, QModelIndex, QSize
from PySide2.QtGui import Qt


@dataclass
class Member:
    id: int

    def __str__(self):
        return "Member " + str(self.id)


@dataclass
class Room:
    id: int
    name: str
    members: List[Member]

    def __init__(self, id: int, name: str, members: List[Member]):
        self.id = id
        self.name = name
        self.members = members


class RoomsModel(QAbstractListModel):
    def __init__(self, rooms: List[Room]):
        super().__init__()
        self.rooms = rooms

    def rowCount(self, parent=None):
        return len(self.rooms)

    def get_room_at_row(self, row: int) -> Room:
        return self.rooms[row]

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if role == Qt.SizeHintRole:
            return QSize(253, 40)
        if role == Qt.DisplayRole:
            room = self.rooms[index.row()]
            return room.name

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        res = True
        self.beginRemoveRows(QModelIndex(), row, row + count)
        while count > 0:
            try:
                self.rooms.pop(row)
                count -= 1
            except IndexError:
                res = False
        self.endRemoveRows()
        return res


class MembersModel(QAbstractListModel):
    def __init__(self, members: List[Member]):
        super().__init__()
        self.members = members

    def rowCount(self, parent=None) -> int:
        return len(self.members)

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if role == Qt.SizeHintRole:
            return QSize(253, 40)
        if role == Qt.DisplayRole:
            member = self.members[index.row()]
            return str(member)

    def reset(self, members: List[Member]):
        self.beginResetModel()
        self.members = members
        self.endResetModel()

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        res = True
        self.beginRemoveRows(QModelIndex(), row, row + count)
        try:
            while count > 0:
                self.members.pop(row)
                count -= 1
        except IndexError:
            res = False
        self.endRemoveRows()
        return res

    def remove_at_indexes(self, indexes: List[int]):
        res = True
        indexes.sort()
        while len(indexes) != 0:
            amount = count_sequential_numbers(indexes)
            if not self.removeRows(indexes[0], amount):
                return False
            indexes = indexes[amount:]
        return res

    def get_first_matching(self, str_repr: str) -> Member:
        for member in self.members:
            if str(member) == str_repr:
                return member


def count_sequential_numbers(numbers: List[int]):
    if len(numbers) == 0:
        return 0

    window_size = 2
    counter = 1
    for i in range(len(numbers) - window_size + 1):
        l, r = numbers[i: i + window_size]
        if r == l + 1:
            counter += 1
        else:
            break

    return counter


def create_random_members(get_id_func):
    return [Member(get_id_func()) for _ in range(randrange(1, 10))]


def create_rooms(get_id_func):
    return [
        Room(get_id_func, "Room 1", create_random_members(get_id_func)),
        Room(get_id_func, "Room 2", create_random_members(get_id_func)),
        Room(get_id_func, "Room 3", create_random_members(get_id_func)),
        Room(get_id_func, "Room 4", create_random_members(get_id_func)),
        Room(get_id_func, "Room 5", create_random_members(get_id_func)),
    ]
