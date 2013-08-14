#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import reminder
import zen

from config import TAG_TO_EXPORT

def day_one():
    reminder_help_text = 'Export entries with %s tag to Reminder.app' % TAG_TO_EXPORT
    zen_help_text = 'Zen practice'

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reminder', help = reminder_help_text, action= 'store_true')
    parser.add_argument('-z', '--zen', help = zen_help_text, action= 'store_true')
    args = parser.parse_args()

    if args.reminder:
        reminder.export_todo_to_reminder()
    elif args.zen:
        zen.practice_zen()
    else:
        parser.print_help()

if __name__ == '__main__':
    day_one()
