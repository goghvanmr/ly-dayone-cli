# -*- coding: utf-8 -*-

import plistlib
import os
import getpass
import Foundation

def parse_dayone():
	username = getpass.getuser()
	entry_folder_path = '/Users/' + username + '/Library/Mobile Documents/5U8NS4GX82~com~dayoneapp~dayone/Documents/Journal_dayone/entries/'

	for root, dirs, files in os.walk(entry_folder_path):
		for f in files:
			pl = plistlib.readPlist(root + f)

			if 'Tags' not in pl: continue

			if 'TODO' in pl['Tags']:
				entry_text = pl['Entry Text'].replace('"', '\\"')

				reminder_name = entry_text.splitlines()[0] 
				reminder_body = entry_text 
				reminder_list = 'TODO'

				apple_script_command = """
					tell application "Reminders" \n
						make new reminder with properties {body:"%s", name:"%s", container:list "%s"} \n
					end tell
				""" % (reminder_body, reminder_name, reminder_list)

				s = Foundation.NSAppleScript.alloc().initWithSource_(apple_script_command)
				s.executeAndReturnError_(None)

if __name__ == '__main__':
	parse_dayone()
