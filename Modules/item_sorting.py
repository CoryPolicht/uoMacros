import wrapper

class ItemSorting:
    def prompt_properties(self):
        text = "What properties do you want to sort? separate properties with a comma and use the = for a desired value i.e. faster casting = 1, gargoyles only will find faster casting property >= 1 and gargoyles only items"
        return wrapper.message_prompt(text, "properties")

    def _parse_property_response(self, raw_property_list):
        # type: (str) -> dict[str, str]
        property_list = self._parse_raw_property_list(raw_property_list)
        property_dict = {}  # type: dict[str, str]
        for property_in_message in property_list:
            property_dict.update(
                self._check_for_property_value_or_default(property_in_message, ""))
        return property_dict

    def _create_key_pair(self, key, value):
        # type: (str, str) -> dict[str, str]
        return {key: value}

    def _check_for_property_value_or_default(self, property_message, default):
        # type: (str, str) -> dict[str, str]
        if "=" in property_message:
            property_and_value = self._get_property_and_value_from_message(
                property_message)
            return self._create_key_pair(property_and_value[0], property_and_value[1])
        return self._create_key_pair(property_message, default)

    def _get_property_and_value_from_message(self, property_message):
        split_message = property_message.split("=")
        return split_message

    def _parse_raw_property_list(self, raw_property_response):
        # type: (str) -> list[str]
        return raw_property_response.split(",")

    def _set_source_destination(self):
        source = wrapper.prompt_alias("source")
        destination = wrapper.prompt_alias("destination")
        return (source, destination)

    def sort_items(self):
        # type: () -> None
        source, destination = self._set_source_destination()
        property_dict = {}
        res, response = self.prompt_properties()
        if res:
            property_dict = self._parse_property_response(response)
        else:
            return
        item_list = wrapper.get_all_items_from_cont(source)
        for item in item_list:
            if self.check_all_properties(item, property_dict):
                wrapper.move_item(item, destination)
                wrapper.pause(1000)

    def check_property_value(self, item_id, property_name, property_value_to_match):
        # type: (int, str, str) -> bool
        property_value_str = wrapper.property_value(item_id, property_name)
        return int(property_value_str) >= int(property_value_to_match)

    def check_all_properties(self, item_id, property_dict):
        # type: (int, dict[str, str]) -> bool
        for k, v in property_dict.items():
            if wrapper.property(item_id, k):
                if v:
                    return self.check_property_value(item_id, k, v)
                else:
                    return True
        return False

    def move_all(self):
        # type: () -> None
        source, destination = self._set_source_destination()
        items_to_trash = wrapper.get_all_items_from_cont(source)
        for item in items_to_trash:
            wrapper.move_item(item, destination)
            wrapper.pause(1000)

    def move_items_by_name(self):
        source, destination = self._set_source_destination()
        res, item_name = wrapper.message_prompt("Name of item?", "name")
        if not res:
            return
        items = wrapper.find_items_by_name(item_name, source)
        for item in items:
            wrapper.move_item(item, destination)
            wrapper.pause(1000)

