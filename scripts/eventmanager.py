from .events import Event
from datetime import datetime, timedelta

_OPTIONS = ["-d", "-t", "-r", "-s"]
allEvents = []


def format_date(date):
    if len(date) == 0:
        return None
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if 'a' in date:
        for day in weekdays:
            if day in date.lower() and len(date.split()) == 1:
                current_weekday = datetime.today().weekday()
                desired_weekday = weekdays.index(day)
                days_from_now = desired_weekday - current_weekday
                if days_from_now < 0:
                    days_from_now += 7
                date = str(datetime.now() + timedelta(days=days_from_now))
                return date
    if '/' in date:
        nums = date.split('/')
        print(nums)
    if '-' in date:
        nums = date.split('-')
        print(nums)
    return None


def format_time(time, date):
    return None


def set_name(args):
    if args[0] is None or args[0] in _OPTIONS:
        return None
    name = ''
    for w in args:
        if w not in _OPTIONS:
            name += ' ' + w
        else:
            break
    return name


def set_date(args):
    if '-d' not in args:
        return str(datetime.now() + timedelta(days=1))
    date = ''
    try:
        current_index = args.index("-d") + 1
        while not current_index >= len(args) and args[current_index] not in _OPTIONS:
            date += ' ' + args[current_index]
            current_index += 1
        date = format_date(date)
        print(date)
    except IndexError:
        print("You forgot a date after '-d'! Try '5/12', or 'Friday'!")
    except:
        pass
    return date if date is not None else None


def set_time(args, date):
    time = ''
    try:
        current_index = args.index("-t") + 1
        while not current_index >= len(args) and args[current_index] not in _OPTIONS:
            time += ' ' + args[current_index]
            current_index += 1
        time = format_time(time, date)
    except:
        print("There was a problem parsing your time. We got \n" + time)
    return time if time is not None else None


def set_summary(args):
    if '-s' not in args:
        return None
    summary = ''
    try:
        current_index = args.index("-s") + 1
        while not current_index >= len(args) and args[current_index] not in _OPTIONS:
            summary += ' ' + args[current_index]
            current_index += 1
    except:
        print("There was a problem parsing your summary. We got \n"+summary)
    return summary


def set_role(args):
    role = "@here"
    try:
        role = args[args.index("-r") + 1]
    except IndexError:
        print("You forgot a role after '-r'! Try 'here', or '@HTML Team'!")
    except:
        pass
    if '@' in role:
        role = role.replace('@', '')
    return role


def parse(myInp):
    args = myInp.split()
    if len(args) == 0:
        print("No arguments.")
        return
    name = set_name(args)
    if name is None:
        return
    date = set_date(args)
    return Event(name, date, set_time(args, date), set_summary(args), set_role(args))


# !sch add <eventName> [OPTIONS]
# Options:
# -d <date>
# -t <time>
# -s <summary>
# -r <role>


def add_event(myInp, myEvents=None):
    if myEvents is None:
        myEvents = allEvents
    e = parse(myInp)
    print(myInp)
    for i in myEvents:
        if i.getName() == e.getName():
            return "This eventname already exists! Maybe you meant to edit?"
    if e is None:
        return "Failed to add event."
    myEvents.append(e)
    return "Added event successfully. It should show up in the event list."


def edit_event(myInp, myEvents):
    e = parse(myInp)
    print("Editing events")

