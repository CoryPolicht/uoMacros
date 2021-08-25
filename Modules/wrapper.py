from ClassicAssist.Data.Macros.Commands.GumpCommands import *
from ClassicAssist.Data.Macros.Commands.ObjectCommands import *
from ClassicAssist.Data.Macros.Commands.MainCommands import *
from ClassicAssist.Data.Macros.Commands.ObjectCommands import *
from ClassicAssist.Data.Macros.Commands.AliasCommands import *
from ClassicAssist.Data.Macros.Commands.JournalCommands import *
from ClassicAssist.Data.Macros.Commands.ActionCommands import *
from ClassicAssist.Data.Macros.Commands.PropertiesCommands import *
from Assistant import Engine
#from types import Any, Tuple

def find_alias(alias_name):
    # type: (str) -> int
    return FindAlias(alias_name)

def prompt_alias(alias_name):
    # type: (str) -> int
    return PromptAlias(alias_name)

def sys_message(message, hue = 1389):
    # type: (str, int) -> None
    SysMessage(message, hue)

def pause(miliseconds):
    # type: (int) -> None
    Pause(miliseconds)

def reply_gump(gump_id, response):
    # type: (int, int) -> None
    ReplyGump(gump_id, response)

def wait_for_gump(gump, miliseconds):
    # type: (int, int) -> None
    WaitForGump(gump, miliseconds)

def use_object(object_serial):
    # type: (int) -> None
    UseObject(object_serial)

def use_type(object_serial):
    # type: (int) -> None
    UseType(object_serial)

def in_gump(gump_id, text):
    # type: (int, str) -> bool
    return InGump(gump_id, text)

def get_gump(gump_id):
    # type: (int)
    return Engine.Gumps.GetGumps(gump_id)

def wait_for_contents(container, timeout):
    # type: (int, int) -> None
    WaitForContents(container, timeout)

def get_items(container):
    # type: (int) -> list
    return Engine.Items.GetItem(container)

def wait_for_target(timeout):
    # type: (int) -> None
    WaitForTarget(timeout)

def target(item_id):
    # type: (int) -> None
    Target(item_id)

def get_alias(alias):
    # type: (str) -> int
    return GetAlias(alias)

def property(item_id, property_name):
    # type: (int, str) -> bool
    return Property(item_id, property_name)

def move_item(item_id, location):
    # type: (int, int | str) -> None
    MoveItem(item_id, location)

def move_type(item_graphic, source, destination):
    #type: (int, int | str, int | str) -> None
    MoveType(item_graphic, source, destination)

def property_value(object_id, property_name):
    #type: (int, str) -> Any
    return PropertyValue[str](object_id, property_name)

def find_items_by_name(name, container):
    # type: (str, int) -> list[int]
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

def get_all_items_from_cont(container_id):
    # type: (int) -> list[int]
    items = []
    cont = Engine.Items.GetItem(container_id)
    if cont == None:
	    return
    if cont.Container == None:
	    WaitForContents(container_id, 5000)

    for item in cont.Container.GetItems():
        items.append(item.Serial)
    return items

def message_prompt(gump_text, initial_text):
    # type: (str, str) -> Tuple[bool, str]
    return MessagePrompt(gump_text, initial_text)
