import crafting
import gumps
import item_types
import common

class Tailoring(crafting.Crafting):

    no_material = ""

    craft_responses = {
        1: common.created,
        2: common.exceptional,
        3: no_material
    }

    tailoring_category_dict = {
        "hats": 1,
        "shirts": 8,
        "pants": 15,
        "miscellaneous": 22,
        "footware": 29,
        "leather armor": 36,
        "studded armor": 43,
        "female armor": 50,
        "bone armor": 57,
        "cloth armor": 64,
        "leather type": 7,
        "make last": 21
    }
    hat_dict = {}
    shirt_dict = {}
    pants_dict = {}
    misc_dict = {}
    footware_dict = {}
    leather_armor_dict = {}
    studded_leather_dict = {}
    female_dict = {}
    bone_dict = {}
    cloth_dict = {}
    leather_type_dict = {}

    def __init__(self):
        factory = gumps.GumpResponseMapFactory()
        tailoring_map = factory.create_map(self.tailoring_category_dict)
        tailoring_map.update(factory.create_map(self.hat_dict, "hats"))
        tailoring_map.update(factory.create_map(self.shirt_dict, "shirts"))
        tailoring_map.update(factory.create_map(self.pants_dict, "pants"))
        tailoring_map.update(factory.create_map(self.misc_dict, "miscellaneous"))
        tailoring_map.update(factory.create_map(self.footware_dict, "footware"))
        tailoring_map.update(factory.create_map(self.leather_armor_dict, "leather armor"))
        tailoring_map.update(factory.create_map(self.studded_leather_dict, "studded armor"))
        tailoring_map.update(factory.create_map(self.female_dict, "female armor"))
        tailoring_map.update(factory.create_map(self.bone_dict, "bone armor"))
        tailoring_map.update(factory.create_map(self.cloth_dict, "cloth armor"))
        tailoring_map.update(factory.create_map(self.leather_type_dict, "leather type"))
        super().__init__("tailoring", item_types.SEWING_KIT, self.craft_responses, tailoring_map)
