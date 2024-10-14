class Player():
    def __init__(self, name, job, max_hp, current_hp, defense, attack, damage, head, torso, hand_1, hand_2, legs):
        self.game_over = False
        self.name = name
        self.job = job
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.defense = defense
        self.attack = attack
        self.damage = damage
        self.head = head
        self.torso = torso
        self.hand_1 = hand_1
        self.hand_2 = hand_2
        self.legs = legs

class Monster():
    def __init__(self, name, hp, defense, attack, damage):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.damage = damage

class Item():
    def __init__(self, type, defense, attack, damage, slot):
        self.type = type
        self.defense = defense
        self.attack = attack
        self.damage = damage
        self.slot = slot