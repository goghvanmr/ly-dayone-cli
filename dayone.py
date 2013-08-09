#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import reminder

from config import TAG_TO_EXPORT 

parser = argparse.ArgumentParser()
help_text = 'Export entries with %s tag to Reminder.app' % TAG_TO_EXPORT
parser.add_argument('-r', '--reminder', help = help_text, action= 'store_true')
args = parser.parse_args()

if args.reminder:
    reminder.export_todo_to_reminder()
else:
    parser.print_help()
