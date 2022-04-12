from default_classe import *

class Comrade(Charactrer):
    def hang_out(self):
        print(f"Now you are going togeteher with {self.name}")

class Street(Room):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.linked_streets = dict()

    def link_street(self, other, direcrion):
        self.linked_streets[direcrion] = other
