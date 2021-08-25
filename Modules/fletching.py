import crafting
import common
import gumps

class Fletching(crafting.Crafting):

    no_wood = ""

    craft_response = {
        1: common.created,
        2: common.exceptional,
        3: no_wood
    }

    fletching_category_dict = {
        "" : 1
    }

    def __init__(self):
        factory = gumps.GumpResponseMapFactory()
        fletching_map = factory.create_map(self.fletching_category_dict)
        fletching_map.update(factory.create_map())
