import common
import blacksmith
import wrapper
import bulk_order
import item_types

class BlacksmithBulkOrder(bulk_order.BulkOrder):

	def __init__(self):	
		super().__init__()
		self._craft = blacksmith.BlacksmithCrafting()
		self._setup()

	def start(self):
		self.use_deed()
		requires_exceptional = self._gump_nav.check_in_gump("exceptional")
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
		wrapper.move_type(item_types.BULK_ORDER_DEED, "backpack", "complete bag")

	def _setup(self):
		common.checkOrMakeAlias("salvage bag")
		common.checkOrMakeAlias("complete bag")
		self._backpack_id = wrapper.get_alias("backpack")

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
			if self._gump_nav.check_in_gump(k):
				return k
		return "iron"
