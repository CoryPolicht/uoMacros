import common
import wrapper

class GumpResponseMapFactory:
    def create_map(self, dictionary_map, parent_map_name=None):
        # type: (dict[str, int], str) -> dict[str, GumpResponseMap]
        new_map = {}
        for k, v in dictionary_map.items():
            if parent_map_name:
                new_map[k] = GumpResponseMap(k, v, parent_map_name)
            else:
                new_map[k] = GumpResponseMap(k, v)
        return new_map


class GumpResponseMap:
    def __init__(self, name, response, parent_map_name = None):
        # type: (str, int, str) -> None
        self.name = name
        self.Response = response 
        self.parent_map_name = parent_map_name

    # in the event I want to use this as a key in dict
    def __hash__(self):
        return hash(str(self.name))

    def __eq__(self, other):
        if isinstance(other, GumpResponseMap):
            return self.name == other.name
        return False


class GumpNavigation:
    def __init__(self, gump_id, gump_map):
        self._gump_id = gump_id
        self._gump_map = gump_map

    def gump_response(self, response):
        # type: (int) -> None
        common.gump_response(self._gump_id, response)

    # recursive so I don't need to iterate over whole list
    # make sure useTool is called before this
    def navigate_gump(self, item_name):
        if self._gump_map[item_name].parent_map_name:
            parent_response = self._gump_map[item_name].parent_map_name
            self.navigate_gump(parent_response)
        response = self._gump_map[item_name].parent_map_name
        self.gump_response(response)

    def get_element_text_by_xy(self, x_cords, y_cords):
        res, gump = wrapper.get_gump(self._gump_id)
        # todo wrap this in an abstract way
        element = gump.GetElementByXY(x_cords, y_cords)
        return element.Text

    # takes only dictionary object returns any matching items
    def check_in_gump(self, value):
        return wrapper.in_gump(self._gump_id, value)
