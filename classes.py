class Player():
    def __init__(self, name, job, max_hp, current_hp, defense, attack, damage, head_count, torso_count, arms_count, legs_count):
        self.game_over = False
        self.name = name
        self.job = job
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.defense = defense
        self.attack = attack
        self.damage = damage
        self.head_count = head_count
        self.torso_count = torso_count
        self.arms_count = arms_count
        self.legs_count = legs_count

class Monster():
    def __init__(self, name, hp, defense, damage):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.damage = damage