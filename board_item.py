from datetime import date
import os
from event_log import EventLog
from item_status import ItemStatus

class BoardItem:
    @property
    def status(self):
        return self.__status

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, due_date):
        if due_date < date.today():
            raise ValueError('Due date cant be in the past.')
        try:
            self._history.append(EventLog(f"due_date changed from {self.due_date} to {due_date}"))
        except AttributeError:
            pass
        self.__due_date = due_date

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) < 5 or len(title) > 30:
            raise ValueError('Illegal title length [5:30]')
        try:
            self._history.append(EventLog(f"Title changed from {self.title} to {title}"))
        except AttributeError:
            pass
        self.__title = title

    def add_evt(self,evt_string:str):
        self._history.append(EventLog(evt_string))

    def __init__(self, title: str, due_date: date):
        self._history = []
        self.title = title
        self.due_date = due_date
        self.__status = ItemStatus.OPEN
        self.add_evt(f"Item created : '{self.title}'")

    def history(self):
        return_str = ""
        for log_item in self._history:
            return_str += log_item.info() + os.linesep
        return return_str

    def revert_status(self):
        if self.__status == ItemStatus.previous(self.status):
            self.add_evt(f"Can't change status, already at {self.__status}")
        else:
            self.add_evt(f"Status changed from {self.__status} to {ItemStatus.previous(self.status)}")
        self.__status = ItemStatus.previous(self.status)

    def advance_status(self):
        if self.__status == ItemStatus.next(self.status):
            self.add_evt(f"Can't change status, already at {self.__status}")
        else:
            self.add_evt(f"Status changed from {self.__status} to {ItemStatus.next(self.status)}")
        self.__status = ItemStatus.next(self.status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'
