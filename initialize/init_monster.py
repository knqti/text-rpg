from classes import Monster


def init_monster(monster, monsters_dict:dict):
    stats = monsters_dict[monster]
    monster_name = monster.title()
    
    monster_instance = Monster(
        name = monster_name,
        hp = stats['hp'],
        defense = stats['defense'],
        attack = stats['attack'],
        damage = stats['damage'],
        description = stats['description']
    )
    return monster_instance