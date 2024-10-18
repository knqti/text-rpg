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
    def __init__(self, name, hp, defense, attack, damage, description):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.damage = damage
        self.description = description

class Item():
    def __init__(self, type, defense, attack, damage, slot, description):
        self.type = type
        self.defense = defense
        self.attack = attack
        self.damage = damage
        self.slot = slot
        self.description = description

class Room():
    def __init__(
            self,
            name,
            monster_a,
            monster_b,
            monster_c,
            item_a,
            item_b,
            item_c,
            description,
    ):
        self.name = name
        self.monster_a = monster_a
        self.monster_b = monster_b
        self.monster_c = monster_c
        self.item_a = item_a
        self.item_b = item_b
        self.item_c = item_c
        self.description = description
        