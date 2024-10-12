class Player():
    def __init__(self):
        self.game_over = False
        self.name = ''
        self.job = ''
        self.hp = 10
        self.defense = 0
        self.attack = 0
        self.damage = 0
        self.head_count = 1
        self.torso_count = 1
        self.arms_count = 2
        self.legs_count = 1

class Monster():
    def __init__(self, name, hp, defense, damage):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.damage = damage