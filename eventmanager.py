from .events import *
from .scheduler import *

_OPTIONS = ["-d", "-t", "-r", "-s"]
_myEvents = []


def set_name(args):
    if args[0] is None or args[0] in _OPTIONS:
        return None
    name = args[0]
    for w in args:
        if w not in _OPTIONS:
            name += ' ' + w
        else:
            break
    return name


def set_date(args):
    date = None
    try:
        date = args[args.index("-d") + 1]
    except IndexError:
        print("You forgot a date after '-d'! Try '5/12', or 'Friday'!")
    except:
        pass
    return date


def set_time(args):
    time = None
    try:
        time = args[args.index("-t") + 1]
    except IndexError:
        print("You forgot a time after '-t'! Try '5:30PM', or 'Midnight'!")
    except:
        pass
    return time


def set_summ(args):
    summary = None
    try:
        summary = args[args.index("-s") + 1]
    except IndexError:
        print("You forgot a summary after '-s'! 'Remember to sign your work' is an example.")
    except:
        pass
    return summary


def set_role(args):
    role = "@here"
    try:
        role = args[args.index("-r") + 1]
    except IndexError:
        print("You forgot a role after '-r'! Try 'here', or '@HTML Team'!")
    except:
        pass
    return role


def parse(myInp):
    args = myInp.split()
    if len(args) == 0:
        print("No arguments.")
        return
    name = set_name(args)
    if name is None:
        return

    return Event(name, set_date(args), set_time(args), set_summ(args), set_role(args))


# !sch add <eventName> [OPTIONS]
# Options:
# -d <date>
# -t <time>
# -s <summary>
# -r <role>


def add_event(myInp, myEvents=None):
    if myEvents is None:
        myEvents = _myEvents
    e = parse(myInp)
    print(myInp)
    if e is None:
        return
    for i in myEvents:
        if i.getName() == e.getName():
            print("This eventname already exists! Maybe you meant to edit?")
            return
    myEvents.append(e)


def edit_event(myInp, myEvents):
    e = parse(myInp)
    print("Editing events")