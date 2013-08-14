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

			if not dayone_entry(plist_file): continue

			pl = plistlib.readPlist(plist_file)

			if 'Tags' not in pl: continue

			if TAG_TO_EXPORT in pl['Tags']:
				entry_text = pl['Entry Text'].replace('"', '\\"')

				reminder_command = create_apple_script_command_from(entry_text)
				execute_apple_script_command(reminder_command)

				save_plist(pl, plist_file)


def dayone_entry(plist_file):
	return plist_file.endswith('.doentry')

def create_apple_script_command_from(entry_text):
	reminder_name = entry_text.splitlines()[0]
	reminder_body = entry_text
	reminder_list = REMINDER_LIST

	reminder_command_template = open('reminder.template').read()
	reminder_command = reminder_command_template % (reminder_list, reminder_list, reminder_body, reminder_name, reminder_list)

	return reminder_command

def execute_apple_script_command(command):
	s = Foundation.NSAppleScript.alloc().initWithSource_(command)
	s.executeAndReturnError_(None)

def save_plist(plist, plist_file):
	plist['Tags'].remove(TAG_TO_EXPORT)
	plist['Tags'].append(TAG_AFTER_EXPORT)

	hash_tag = '#%s' % TAG_TO_EXPORT
	plist['Entry Text'] = plist['Entry Text'].replace(hash_tag, '')

	plistlib.writePlist(plist, plist_file)

if __name__ == '__main__':
	export_todo_to_reminder()
