import crafting
import gumps
import common
import item_types

class Tinkering(crafting.Crafting):
    no_material = ""
    
    craft_response = {
        1: common.created,
        2: common.exceptional,
        4: no_material
    }

    tinkering_category_dict = {
        "wood": 1,
        "tools": 8,
        "parts": 15,
        "utensils": 22,
        "miscellaneous": 29,
        "jewelry": 36,
        "assemblies": 43,
        "traps": 50,
        "customs": 57,
        "magic jewelry": 64,
        "material type": 7,
        "make last": 21
    }
    wooden_items_dict = {}
    tools_dict = {}
    parts_dict = {}
    utensils_dict = {}
    misc_dict = {
        "spyglass": 37
    }
    jewelry_dict = {}
    assemblies_dict = {}
    traps_dict = {}
    customs_dict = {}
    magic_jewelry = {}

    def __init__(self):
        factory = gumps.GumpResponseMapFactory()
        tinkering_map = factory.create_map(self.tinkering_category_dict)
        tinkering_map.update(factory.create_map(self.wooden_items_dict, "wood"))
        tinkering_map.update(factory.create_map(self.parts_dict, "parts"))
        tinkering_map.update(factory.create_map(self.utensils_dict, "utensils"))
        tinkering_map.update(factory.create_map(self.misc_dict, "miscellaneous"))
        tinkering_map.update(factory.create_map(self.jewelry_dict, "jewelry"))
        tinkering_map.update(factory.create_map(self.assemblies_dict, "assemblies"))
        tinkering_map.update(factory.create_map(self.traps_dict, "traps"))
        tinkering_map.update(factory.create_map(self.customs_dict, "customs"))
        tinkering_map.update(factory.create_map(self.magic_jewelry, "magic jewelry"))
        super().__init__("tinkering", item_types.TOOL_KIT, self.craft_response, tinkering_map)
