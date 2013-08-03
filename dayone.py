# -*- coding: utf-8 -*-

import plistlib
import os
import getpass

def parse_dayone():
	username = getpass.getuser()
	entry_folder_path = '/Users/' + username + '/Library/Mobile Documents/5U8NS4GX82~com~dayoneapp~dayone/Documents/Journal_dayone/entries/'

	for root, dirs, files in os.walk(entry_folder_path):
		for f in files:
			pl = plistlib.readPlist(root + f)

			if 'Tags' not in pl: continue

			if 'TODO' in pl['Tags']:
				print pl['Entry Text']

if __name__ == '__main__':
	parse_dayone()
