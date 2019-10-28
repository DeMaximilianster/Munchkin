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
        self.card_pic = str()


class Race(Card):
    def __init__(self, func=None):
        Card.__init__(self)
        self.leave_bonus = int()
        self.skill = func


class Role(Card):
    def __init__(self, func_1=None, func_2=None):
        Card.__init__(self)
        self.skill_1 = func_1
        self.skill_2 = func_2


class Treasure(Card):
    def __init__(self):
        Card.__init__(self)
        self.price = int()
        self.type = str()
        self.bonus = int()

        self.one_time = bool()


class Monster(Card):
    def __init__(self, func=None):
        Card.__init__(self)
        self.indecency = func
        self.level = int()
        self.level_reward = int()
        self.treasure_reward = int()

        self.ignorance = dict()  # Манчины, которых монстр не трогает (хмм, или лучше сделать лямбда-функцией)
        self.ignorance_special = None  # Особый эффект для игнорируемых Манчкинов (смотри карту "Амазонка")
        self.is_undead = bool()
