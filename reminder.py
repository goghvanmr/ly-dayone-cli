# -*- coding: utf-8 -*-

import plistlib
import os
import getpass
import Foundation

from config import *

JOURNAL_ENTRIES_PATH = '/Library/Mobile Documents/5U8NS4GX82~com~dayoneapp~dayone/Documents/Journal_dayone/entries/' 

def export_todo_to_reminder():
	username = getpass.getuser()
	entry_folder_path = '/Users/' + username + JOURNAL_ENTRIES_PATH  
	
	for root, dirs, files in os.walk(entry_folder_path):
		for f in files:
			plist_file = root + f

			if not plist_file.endswith('.doentry'): continue

			pl = plistlib.readPlist(plist_file)

			if 'Tags' not in pl: continue

			if TAG_TO_EXPORT in pl['Tags']: 
				entry_text = pl['Entry Text'].replace('"', '\\"')

				reminder_name = entry_text.splitlines()[0] 
				reminder_body = entry_text
				reminder_list = REMINDER_LIST

				reminder_command_template = open('reminder.template').read()
				reminder_command = reminder_command_template % (reminder_list, reminder_list, reminder_body, reminder_name, reminder_list)

				s = Foundation.NSAppleScript.alloc().initWithSource_(reminder_command)
				s.executeAndReturnError_(None)

				pl['Tags'].remove(TAG_TO_EXPORT)
				pl['Tags'].append(TAG_AFTER_EXPORT)
				plistlib.writePlist(pl, plist_file)

if __name__ == '__main__':
	export_todo_to_reminder()
