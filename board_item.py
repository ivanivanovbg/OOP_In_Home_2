from datetime import date
from item_status import ItemStatus


class BoardItem:
    def __init__(self, title: str, due_date: date):
        if (len(title) < 5 or len(title) > 30):
            raise ValueError('Illegal title length [5:30]')
        if (due_date < date.today()):
            raise ValueError('Due date cant be in the past.')

        self.title = title
        self.due_date = due_date
        self.status = ItemStatus.OPEN

    def revert_status(self):
        self.status = ItemStatus.previous(self.status)

    def advance_status(self):
        self.status = ItemStatus.next(self.status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'
