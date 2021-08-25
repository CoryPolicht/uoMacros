import common
import wrapper
import gumps

class Crafting:
    def __init__(self, name, tool_gump, tool, craft_result_map, gump_map):
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
        for k, v in self._craft_result_map.items():
            if wrapper.in_gump(self._tool_gump, v):
                return k
        return -1

    def select_option(self, gump_response_name):
        self.GumpNav.navigate_gump(gump_response_name)

