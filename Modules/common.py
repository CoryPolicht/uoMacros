from ClassicAssist.Data.Macros.Commands.MainCommands import *
from ClassicAssist.Data.Macros.Commands.GumpCommands import *
from ClassicAssist.Data.Macros.Commands.ObjectCommands import *
from ClassicAssist.Data.Macros.Commands.AliasCommands import *
from ClassicAssist.Data.Macros.Commands.JournalCommands import *

def checkOrMakeAlias(aliasName):
	if not FindAlias(aliasName):
		PromptAlias(aliasName)

def throwError(msg, severity = 1):
	#db.log(msg, severity)
    SysMessage(msg, 1652)

def gumpResponse(gump, response):
	Pause(1000)
	ReplyGump(gump, response)
	WaitForGump(gump, 5000)

def useObjectAndGumpResponse(itemSerial, gump, response):
	UseObject(itemSerial)
	WaitForGump(gump, 5000)
	gumpResponse(gump, response)

def useTypeAndGumpResponse(serial, gump, response):
	UseType(serial)
	WaitForGump(serial, 5000)
	gumpResponse(gump, response)
	