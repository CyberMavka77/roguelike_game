class Room:
    def __init__(self, name) -> None:
        self.name = name
        self.linked = dict()
        self.character = None
        self.items = None

    def set_description(self, description):
        self.description = description

    def link_room(self, other, direcrion):
        self.linked[direcrion] = other

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.items = item
    
    def get_item(self):
        return self.items

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direct in self.linked:
            print(f"the {self.linked[direct].name} is {direct}")

    def get_character(self):
        return self.character

    def move(self, direction):
        if direction in self.linked:
            return self.linked[direction]
        else:
            print("No room in such direction")

class Charactrer:
    def __init__(self, name, descr) -> None:
        self.name, self.description = name, descr

    def set_conversation(self, words):
        self.words = words

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        print(self.words)

class Enemy(Charactrer):
    defeated = 0
    def __init__(self, name, descr) -> None:
        super().__init__(name, descr)
        self.weaknesses = []

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, weapon):
        if weapon == self.weakness:
            Enemy.defeated += 1
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self):
        return Enemy.defeated

class Item:
    def __init__(self, name) -> None:
        self.name = name

    def set_description(self, descr):
        self.description = descr

    def get_name(self):
        return self.name
    
    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")
