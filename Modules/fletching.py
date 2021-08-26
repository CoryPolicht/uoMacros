import crafting
import common
import gumps
import item_types

class Fletching(crafting.Crafting):

    no_wood = ""

    craft_response = {
        1: common.created,
        2: common.exceptional,
        3: no_wood
    }

    fletching_category_dict = {
        "materials" : 1,
        "ammunition": 8,
        "weapons": 15,
        "boards": 7,
        "make last": 21
    }

    material_dict = {}
    ammunition_dict = {}
    weapons_dict = {}
    craft_material_dict = {}

    def __init__(self):
        factory = gumps.GumpResponseMapFactory()
        fletching_map = factory.create_map(self.fletching_category_dict)
        fletching_map.update(factory.create_map(self.material_dict, "materials"))
        fletching_map.update(factory.create_map(self.ammunition_dict, "ammunition"))
        fletching_map.update(factory.create_map(self.weapons_dict, "weapons"))
        fletching_map.update(factory.create_map(self.craft_material_dict, "boards"))
        super().__init__("fletching", item_types.ARROW_FLETCHING, self.craft_response, fletching_map)
