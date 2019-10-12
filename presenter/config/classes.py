class Munchkin:
    def __init__(self):
        self.id = int()
        self.name = str()

        self.level = int()
        self.gender = str()

        self.race = Race()
        self.role = Role()

        self.has_class_weaknesses = bool()
        self.has_role_weaknesses = bool()

        self.helm = Treasure()
        self.armor = Treasure()
        self.boots = Treasure()
        self.in_hand = list()
        self.other = list()

        self.free_arm = bool()
        self.can_pick_big_item = bool()


class Card:
    def __init__(self):
        pass


class Race(Card):
    pass


class Role(Card):
    pass


class Treasure(Card):
    pass


class OneTime(Card):
    pass
