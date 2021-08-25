import item_types
import crafting
import gumps
import common


class BlacksmithCrafting(crafting.Crafting):
    no_Metal = "you do not have sufficient metal to make that"

    craft_responses = {
        1: common.created,
        2: common.exceptional,
        3: no_Metal
    }
    blacksmith_category_dict = {
        "ringmail": 1,
        "chainmail": 8,
        "platemail": 15,
        "helmets": 22,
        "shields": 29,
        "throwing": 36,
        "bladed": 43,
        "axes": 50,
        "polearms": 57,
        "bashing": 64,
        "dragon scale armor": 71,
        "metal type": 7,
        "make last": 21
    }
    ringmail_dict = {}
    chainmail_dict = {
        "chainmail coif": 2,
        "chainmail leggings": 9,
        "chainmail tunic": 16
    }
    platemail_dict = {}
    helmet_dict = {
        "bascinet": 2,
        "close helmet": 9,
        "helmet": 16,
        "norse helm": 23,
        "plate helm": 30
    }
    shield_dict = {
        "metal shield": 23
    }
    throwing_dict = {}
    blade_dict = {
        "cutlass": 23,
        "dagger": 30,
        "katana": 37,
        "kryss": 44
    }
    axe_dict = {}
    polearms_dict = {
        "halbred": 23,
        "war fork": 65
    }
    bashing_dict = {
        "hammer pick": 2,
        "mace": 9,
        "maul": 16,
        "scepter": 23,
        "war mace": 30
    }
    dragon_dict = {}
    metal_type_dict = {
        "iron": 6,
        "dull copper": 13,
        "shadow iron": 20,
        "copper": 27,
        "bronze": 34,
        "gold": 41,
        "agapite": 48,
        "verite": 55,
        "valorite": 62,
        "blaze": 69,
        "ice": 76,
        "toxic": 83,
        "electrum": 90,
        "platinum": 97,
        "red scales": 0,
        "yellow scales": 0,
        "black scales": 0,
        "green scales": 0,
        "white scales": 0,
        "blue scales": 0,
        "copper scales": 0,
        "silver scales": 0,
        "gold scales": 0
    }

    def __init__(self):
        factory = gumps.GumpResponseMapFactory()
        # make category Map
        blacksmith_map = factory.create_map(self.blacksmith_category_dict)
        # metal type map
        blacksmith_map.update(factory.create_map(
            self.metal_type_dict, "metal type"))
        # add the rest of the maps
        blacksmith_map.update(factory.create_map(
            self.ringmail_dict, "ringmail"))
        blacksmith_map.update(factory.create_map(
            self.chainmail_dict, "chainmail"))
        blacksmith_map.update(factory.create_map(
            self.platemail_dict, "platemail"))
        blacksmith_map.update(factory.create_map(self.helmet_dict, "helmets"))
        blacksmith_map.update(factory.create_map(self.shield_dict, "shields"))
        blacksmith_map.update(factory.create_map(
            self.throwing_dict, "throwing"))
        blacksmith_map.update(factory.create_map(self.blade_dict, "bladed"))
        blacksmith_map.update(factory.create_map(self.axe_dict, "axes"))
        blacksmith_map.update(factory.create_map(
            self.polearms_dict, "polearms"))
        blacksmith_map.update(factory.create_map(self.bashing_dict, "bashing"))
        blacksmith_map.update(factory.create_map(
            self.dragon_dict, "dragon scale armor"))
        super().__init__("blacksmith",
                         item_types.SMITH_HAMMER, self.craft_responses, blacksmith_map)
