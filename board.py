from board_item import BoardItem
class Board:
    def __init__(self):
        self._items = []

    def add_item(self,b_item:BoardItem,val_err:bool=False):
        if not b_item in self._items:
            self._items.append(b_item)
        else:
            if val_err:
                raise ValueError("Item already in the list")
    @property
    def count(self):
        return len(self._items)