from datetime import datetime
class EventLog():
    def __init__(self, description: str):
        self._description = description
        #15-September-2020 11:36:32
        self._timestamp = str(datetime.now().strftime("%d-%B-%y %H:%M:%S"))

    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self):
        return f"[{self.timestamp}] {self.description}"
