from datetime import date, timedelta
from board import Board
from board_item import BoardItem


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
