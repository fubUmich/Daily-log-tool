from logger_helper import *
import datetime
import argparse

parser = argparse.ArgumentParser(description='parse log command')
parser.add_argument('-s', action='store_true', help='Show logs')
parser.add_argument('-d', default='today', help='Specify a date to show log, like "today", "yesterday", "2016-03-05"')
parser.add_argument('-l', help='write a log')
parser.add_argument('-ra', action='store_true', help='Remove todays log totally')
parser.add_argument('-r', default=1, help='How many logs to delete')

args = parser.parse_args()

if args.s:
    date = args.d
    show_log(date)

elif args.l:
    write_log(args.l)

elif args.ra:
    print "Are your sure you want to remove today's log? [y/n]"
    choice = raw_input().lower()
    if choice == 'y':
        remove_whole_log()

elif args.r:
    remove_last_log(args.r)

else:
    pass