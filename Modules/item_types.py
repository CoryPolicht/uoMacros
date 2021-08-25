
LOCK_PICKS = 0x14fc
SMITH_HAMMER = 0x13e3
BULK_ORDER_BOOK = 0x2259
SEWING_KIT = 0xf9d
NAILS = 0x102e
TOOL_KIT = 0x1eb8
ARROW_FLETCHING = 0x1022
BULK_ORDER_DEED = 0x2258


class Item:
    def __init__(self, name, item_id, hue):
        self.name = name
        self.item_id = item_id
        self.hue = hue
