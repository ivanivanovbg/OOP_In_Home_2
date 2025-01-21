from datetime import date
import os
from event_log import EventLog
from item_status import ItemStatus

class BoardItem:
    def __init__(self, title: str, due_date: date):
        self._history = []
        self._title = title
        self._due_date = due_date
        self._status = ItemStatus.OPEN
        self._history.append(EventLog(f"Item created : '{self.title}'"))

    def history(self):
        return_str = ""
        for log_item in self._history:
            return_str += log_item.info() + os.linesep
        return return_str

    @property
    def status(self):
        return self._status

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self,due_date):
        if due_date < date.today():
            raise ValueError('Due date cant be in the past.')
        self._history.append(EventLog(f"due_date changed from {self.due_date} to {due_date}"))
        self._due_date = due_date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        if len(title) < 5 or len(title) > 30:
            raise ValueError('Illegal title length [5:30]')
        self._history.append(EventLog(f"title changed from {self.title} to {title}"))
        self._title = title

    def revert_status(self):
        if self._status == ItemStatus.previous(self.status):
            self._history.append(EventLog(f"Can't change status, already at {self._status}"))
        else:
            self._history.append(EventLog(f"Status changed from {self._status} to {ItemStatus.previous(self.status)}"))
        self._status = ItemStatus.previous(self.status)

    def advance_status(self):
        if self._status == ItemStatus.next(self.status):
            self._history.append(EventLog(f"Can't change status, already at {self._status}"))
        else:
            self._history.append(EventLog(f"Status changed from {self._status} to {ItemStatus.next(self.status)}"))
        self._status = ItemStatus.next(self.status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'
