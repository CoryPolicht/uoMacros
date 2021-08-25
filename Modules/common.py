from wrapper import *

exceptional = "you create an exceptional quality item"
created = "you create the item"

def checkOrMakeAlias(aliasName):
	if not find_alias(aliasName):
		prompt_alias(aliasName)

def throwError(msg, severity = 1):
	#db.log(msg, severity)
    sys_message(msg, 1652)

def gump_response(gump, response):
	pause(1000)
	reply_gump(gump, response)
	wait_for_gump(gump, 5000)

def useObjectAndGumpResponse(itemSerial, gump, response):
	use_object(itemSerial)
	wait_for_gump(gump, 5000)
	gump_response(gump, response)

def useTypeAndGumpResponse(serial, gump, response):
	use_type(serial)
	wait_for_gump(serial, 5000)
	gump_response(gump, response)
	