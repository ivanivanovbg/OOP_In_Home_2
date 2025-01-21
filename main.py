from datetime import date, timedelta,datetime
from board import Board
from board_item import BoardItem


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

item = BoardItem('Refactor this mess', add_days_to_now(2))
item.due_date += timedelta(days=365 * 2)  # two years in the future
item.title = 'Not that important'
item.revert_status()
item.advance_status()
item.revert_status()
print(item.history())

print('\n--------------\n')

anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))
anotherItem.advance_status()
anotherItem.advance_status()
anotherItem.advance_status()
anotherItem.advance_status()
anotherItem.advance_status()
print(anotherItem.history())

item = BoardItem('Refactor this mess', add_days_to_now(2))
anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))

board = Board()
board.add_item(item)
board.add_item(anotherItem)
# val_err is False by default , so no error will be thrown
board.add_item(item) # nothing happens
board.add_item(item) # nothing happens

print(board.count) # 2
# If val_err is True then throw an error
board.add_item(item,True)
board.add_item(anotherItem,True)
board.add_item(item,True)
