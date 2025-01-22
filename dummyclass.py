class Dummyclass():
    def __init__(self):
        self.__nv = "This is not visible outside"
        self._v = "This is visible outside"

    @property
    def nv(self):
        return self.__nv

    @property
    def v(self):
        return self._v
