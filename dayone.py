# -*- coding: utf-8 -*-
import argparse
import reminder

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reminder', help = 'Export TODO entires to reminder.app', action= 'store_true')
args = parser.parse_args()

if args.reminder:
	reminder.export_todo_to_reminder()
else:
	parser.print_help()
