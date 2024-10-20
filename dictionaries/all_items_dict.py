from .armors_dict import *
from .consumables_dict import *
from .weapons_dict import *


all_armors_dict = {
    **armors_1_dict,
    **armors_2_dict
}

all_consumables_dict = {
    **consumables_1_dict
}

all_weapons_dict = {
    **weapons_1_dict,
    **weapons_2_dict
}

all_items_dict = {
    **all_armors_dict,
    **all_consumables_dict,
    **all_weapons_dict
}