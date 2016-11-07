from datetime import date, datetime, timedelta
import os.path

NOW = datetime.now()
TODAY = date.today()
YESTERDAY = TODAY - timedelta(1)


def show_log(date):
    print_log_file(get_log_file_name(date))


def print_log_file(filename):
    if os.path.isfile(filename):
        with open(filename) as log_file:
            print log_file.read()
    else:
        print "No log found for the date"


def get_date_str(date):
    if date == 'today':
        return TODAY
    elif date == 'yesterday':
        return YESTERDAY
    else:
        return date


def get_log_file_name(date):
    date_str = get_date_str(date)
    script_dir = os.path.dirname(__file__)
    return '{script_dir}/logs/{date}.log'.format(script_dir=script_dir, date=str(date_str))


def write_log(log):
    filename = get_log_file_name('today')
    with open(filename, 'a+') as log_file:
        log_file.write('%s %02d:%02d %s\n' % (NOW.date(), NOW.hour, NOW.minute, log))


def remove_whole_log():
    filename = get_log_file_name('today')
    with open(filename, 'w+') as log_file:
        log_file.write("removed at %s:%s\n" % (NOW.hour, NOW.minute))


def remove_last_log(n):
    filename = get_log_file_name('today')
    if os.path.isfile(filename):
        with open(filename, 'r+') as log_file:
            lines = log_file.readlines()
            lines = lines[:-int(n)]

        with open(filename, 'w') as log_file:
            log_file.writelines(lines)
