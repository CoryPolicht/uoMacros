import wrapper

class CraftMenu:
    options_list = ["blacksmith", "tinkering"]

    def get_crafting_option(self):
        wrapper.selection_prompt(self.options_list)