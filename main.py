from datetime import date, timedelta,datetime
from board import Board
from board_item import BoardItem
from event_log import *


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
anotherItem = BoardItem('Encrypt user data', add_days_to_now(10))

item.advance_status()

board = Board()

board.items.append(item)
board.items.append(anotherItem)

for board_item in board.items:
    board_item.advance_status()

for board_item in board.items:
    print(board_item.info())

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