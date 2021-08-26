import wrapper
import gumps

class Crafting:
    def __init__(self, name, tool, craft_result_map, gump_map, tool_gump=0x38920abd):
        # type: (str, int, dict[int, str], dict[str, gumps.GumpResponseMap], int) -> None
        self._name = name
        self._tool_gump = tool_gump
        self._tool = tool
        self._craft_result_map = craft_result_map
        self.GumpNav = gumps.GumpNavigation(tool_gump, gump_map)

    def use_tool(self):
        wrapper.use_type(self._tool)
        wrapper.wait_for_gump(self._tool_gump, 5000)
        wrapper.pause(1000)

    def craft_result(self):
        # type: () -> int
        for k, v in self._craft_result_map.items():
            if wrapper.in_gump(self._tool_gump, v):
                return k
        return -1

    def select_option(self, gump_response_name):
        # type: (str) -> None
        self.GumpNav.navigate_gump(gump_response_name)

    def create_item(self, item, material_selection):
        # type: (str, str) -> int
        self.use_tool()
        # set metal type
        self.select_option(material_selection)
        # make item
        self.select_option(item)
        return self.craft_result()

    def create_last_item(self):
        # type: () -> int
        self.use_tool()
        self.select_option("make last")
        return self.craft_result()
