from Assistant import Engine

def getElementTextByXY(gumpId, xCords, yCords):
    res, gump = Engine.Gumps.GetGump(gumpId)
    element = gump.GetElementByXY(xCords, yCords)
    return element.Text
