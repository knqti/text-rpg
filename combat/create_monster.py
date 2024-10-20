def create_monster(monster, monsters_dict:dict):
    stats = monsters_dict[monster]
    monster_name = str(monster).capitalize()
    
    monster_obj = Monster(
        name=monster_name,
        hp=stats['hp'],
        defense=stats['defense'],
        attack=stats['attack'],
        damage=stats['damage'],
        description=stats['description']
    )
    return monster_obj