class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    __order = (OPEN, TODO, IN_PROGRESS, DONE, VERIFIED)

    @classmethod
    def next(cls, current):
        idx = cls.__order.index(current)
        if idx < len(cls.__order) - 1:
            return cls.__order[idx + 1]
        else:
            return current

    @classmethod
    def previous(cls, current):
        idx = cls.__order.index(current)
        if idx > 0:
            return cls.__order[idx - 1]
        else:
            return current
