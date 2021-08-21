import common
import types
import gumpNavigation
from ClassicAssist.Data.Macros.Commands.GumpCommands import *
from ClassicAssist.Data.Macros.Commands.ObjectCommands import *
from ClassicAssist.Data.Macros.Commands.MainCommands import *

noMetal = "you do not have sufficient metal to make that"
exceptional = "you create an exceptional quality item"
created = "you create the item"

blacksmithGump = 0x38920abd	

craftRespones = {
	1: created,
	2: exceptional,
	3: noMetal
}

blacksmithCategoryGumpSelectionMap = {
	"ringmail": 1,
	"chainmail": 8,
	"platemail": 15,
	"helmet": 22,
	"shield": 29,
	"throwing": 36,
	"bladed": 43,
	"axes": 50,
	"polearms": 57,
	"bashing": 64,
	"dragon": 71
}

poleArmsMap = {
	"halbred": 23,
	"war fork": 65
}

shieldMap = {
	"metal shield": 23
}

bladeMap = {
	"cutlass": 23,
	"dagger": 30,
	"katana": 37,
	"kryss": 44
}

bashingMap = {
	"hammer pick": 2,
	"mace": 9,
	"maul": 16,
	"scepter": 23,
	"war mace": 30
}

chainmailMap = {
	"chainmail coif": 2,
	"chainmail leggings": 9,
	"chainmail tunic": 16
}

helmetMap = {
	"bascinet": 2,
	"close helmet": 9,
	"helmet": 16,
	"norse helm": 23,
	"plate helm": 30 
}
	
blacksmithItemTypeMap = {
	"polearms": poleArmsMap,
	"shield": shieldMap,
	"bladed": bladeMap,
	"bashing": bashingMap,
	"chainmail": chainmailMap,
	"helmet": helmetMap
}

def getCategory(item):
	for key, value in blacksmithItemTypeMap.items():
		if item in value:
			return key

metalTypeResponseMap = {
		"iron": 6,
		"dull copper": 13,
		"shadow iron": 20,
		"copper": 27,
		"bronze": 34,
		"gold": 41,
		"agapite": 48,
		"verite": 55,
		"valorite": 62,
		"blaze": 69,
		"ice": 76,
		"toxic": 83,
		"electrum": 90,
		"platinum": 97,
		"red scales": 0,
		"yellow scales": 0,
		"black scales": 0,
		"green scales": 0,
		"white scales": 0,
		"blue scales": 0,
		"copper scales": 0,
		"silver scales": 0,
		"gold scales": 0
	}

def blacksmithGumpResponse(response):
	common.gumpResponse(blacksmithGump, response)

def setMetalType(metalType):
	blacksmithGumpResponse(7)
	metalResponse = metalTypeResponseMap.get(metalType)
	blacksmithGumpResponse(metalResponse)

def useTool():
	UseType(types.smithHammer)
	WaitForGump(blacksmithGump, 5000)
	Pause(1000)

def getCraftResults():
	for key, value in craftRespones.items():
		if InGump(blacksmithGump, value):
			return key

def createLastItem():
	useTool()
	blacksmithGumpResponse(21)

def createItem(item, metalType):
	category = getCategory(item)
	categoryResponse = blacksmithCategoryGumpSelectionMap.get(category)
	useTool()
	setMetalType(metalType)
	blacksmithGumpResponse(categoryResponse)
	itemList = blacksmithItemTypeMap.get(category)
	itemResponse = itemList.get(item)
	blacksmithGumpResponse(itemResponse)