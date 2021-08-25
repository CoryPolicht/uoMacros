import common
import blacksmith
import wrapper
import gumps


class BlacksmithBulkOrder:
	bulk_order_gump_id = 0x5afbd742
	bulk_order_dict = {"combine": 2}

	def __init__(self):	
		factory = gumps.GumpResponseMapFactory()
		craft = blacksmith.BlacksmithCrafting()
		self._craft = craft
		bulkOrderMap = factory.create_map(self.bulk_order_dict)
		bulk_order_nav = gumps.GumpNavigation(self.bulk_order_gump_id, bulkOrderMap)
		self._bulk_order_nav = bulk_order_nav
		self._setup()

	def start(self):
		wrapper.use_type(0x2258)
		wrapper.wait_for_gump(self.bulk_order_gump_id, 5000)
		requires_exceptional = self._bulk_order_nav.check_in_gump("exceptional")
		metalType = self.get_metal_type()
		item = self.get_item_to_create()
		self._craft.create_item(item, metalType)
		amountToDo = self.get_amount_to_fill()
		haveMetal = True

		while amountToDo > 0 and haveMetal:
			result = self._craft.create_last_item()
			wrapper.pause(2000)
			items_in_bag = wrapper.find_items_by_name(item, self._backpack_id)
			self.check_items_and_fill(requires_exceptional, items_in_bag)
			wrapper.pause(1000)
			haveMetal = result != 3
			amountToDo = self.get_amount_to_fill()
		wrapper.move_type(0x2258, "backpack", "complete bag")

	def _setup(self):
		common.checkOrMakeAlias("salvage bag")
		common.checkOrMakeAlias("complete bag")
		self._backpack_id = wrapper.get_alias("backpack")

	def get_item_to_create(self):
		return self._bulk_order_nav.get_element_text_by_xy(75, 96)
		
	def get_amount_to_make(self):
		result = self._bulk_order_nav.get_element_text_by_xy(275, 48)
		return int(result)

	def get_amount_completed(self):
		result = self._bulk_order_nav.get_element_text_by_xy(275, 96)
		return int(result)

	def get_amount_to_fill(self):
		return self.get_amount_to_make() - self.get_amount_completed()

	def fill_bod(self, item_id):
		self._bulk_order_nav.navigate_gump("combine")
		wrapper.wait_for_target(5000)
		wrapper.target(item_id)

	def check_items_and_fill(self, requires_exceptional, items_in_bag):
		for currentItem in items_in_bag:
			if requires_exceptional:
				if wrapper.property(currentItem, "exceptional"):
					self.fill_bod(currentItem)
				else:
					wrapper.move_item(currentItem, "salvage bag")
			else:
				self.fill_bod(currentItem)

	def get_metal_type(self):
		for k, v in self._craft.metal_type_dict.items():
			if self._bulk_order_nav.check_in_gump(k):
				return k
		return "iron"
