import gumps
import wrapper
import common
import gumps
import item_types

class BulkOrder:
    bulk_order_gump_id = 0x5afbd742
    bulk_order_dict = {"combine": 2}

    def __init__(self):
        factory = gumps.GumpResponseMapFactory()
        bulk_order_map = factory.create_map(self.bulk_order_dict)
        self._gump_nav = gumps.GumpNavigation(self.bulk_order_gump_id, bulk_order_map)

    def use_deed(self):
        wrapper.use_type(item_types.BULK_ORDER_DEED)
        wrapper.wait_for_gump(self.bulk_order_gump_id, 5000)

    def fill_bod(self, item_id):
        # type: (int) -> None
        self._gump_nav.navigate_gump("combine")
        wrapper.wait_for_target(5000)
    
    def get_item_to_create(self):
        # type: () -> str
        return self._gump_nav.get_element_text_by_xy(75, 96)
    
    def get_amount_to_make(self):
        result = self._gump_nav.get_element_text_by_xy(275, 48)
        return int(result)

    def get_amount_completed(self):
        result = self._gump_nav.get_element_text_by_xy(275, 96)
        return int(result)
    
    def get_amount_to_fill(self):
        return self.get_amount_to_make() - self.get_amount_completed()

    def set_requires_exceptional(self):
        self._exceptional = self._gump_nav.check_in_gump("exceptional")
