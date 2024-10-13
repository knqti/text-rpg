class Player():
    def __init__(self, name, job, max_hp, current_hp, defense, attack, damage, head, torso, hand, legs):
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
        self.hand = hand
        self.legs = legs

class Monster():
    def __init__(self, name, hp, defense, damage):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.damage = damage

class Item():
    def __init__(self, type, defense, attack, damage, slot_name, slot_value):
        self.type = type
        self.defense = defense
        self.attack = attack
        self.damage = damage
        self.slot_name = slot_name
        self.slot_value = slot_value