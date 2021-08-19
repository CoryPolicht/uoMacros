from Assistant import Engine

# # public macro from reetus
def FindItemsByName(name, container):
	items = []
	
	cont = Engine.Items.GetItem(container)
	
	if cont == None:
		return
		
	if cont.Container == None:
		WaitForContents(container, 5000)
		
	for item in cont.Container.GetItems():
		if item.Name.ToLower().Contains(name.ToLower()):
			items.append(item.Serial)	
	
	return items

def hasProperty(itemId, itemProperty):
    result = False
    item = Engine.Items.GetItem(itemId)
    if itemProperty in item.Properties:
        result = True
    return result