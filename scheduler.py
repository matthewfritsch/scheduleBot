import datetime

now = datetime.datetime.now()

current_date = datetime.date.today()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Current Date =", current_date)


OPTIONS = ["-d","-t","-r","-s"]
myEvents = []

inp = ""


class Event:
    def __init__(self, name, date, time, summ, role):
        self.name = name
        self.date = date
        self.time = time
        self.role = role
        self.summ = summ

    def __repr__(self):
        toRet = "Event: \n--Name: " + self.name
        if self.date is not None:
            toRet = toRet + "\n--Date: " + self.date
        if self.time is not None:
            toRet = toRet + "\n--Time: " + self.time
        if self.summ is not None:
            toRet = toRet + "\n--Summ: " + self.summ
        if self.role is not None:
            toRet = toRet + "\n--Role: " + self.role
        return toRet + "\n"

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getRole(self):
        return self.role

    def getSumm(self):
        return self.summ

    def setName(self, name):
        self.name = name
    
    def setDate(self, date):
        self.date = date
    
    def setTime(self, time):
        self.time = time
    
    def setRole(self, role):
        self.role = role
 
    def setSumm(self, summ):
        self.summ = summ


def setName(args):
    return args[0] if args[0] not in OPTIONS else None

def setDate(args):
    date = None
    try:
        date = args[args.index("-d")+1]
    except IndexError:
        print("You forgot a date after '-d'! Try '5/12', or 'Friday'!")
    except:
        pass
    return date

def setTime(args):
    time = None
    try:
        time = args[args.index("-t")+1]
    except IndexError:
        print("You forgot a time after '-t'! Try '5:30PM', or 'Midnight'!")
    except:
        pass
    return time

def setSumm(args):
    summ = None
    try:
        summ = args[args.index("-s")+1]
    except IndexError:
        print("You forgot a summary after '-s'! 'Remember to sign your work' is an example.")
    except:
        pass
    return summ

def setRole(args):
    role = "@here"
    try:
        role = args[args.index("-r")+1]
    except IndexError:
        print("You forgot a role after '-r'! Try 'here', or '@HTML Team'!")
    except:
        pass
    return role

def parse(myInp):
    name = date = time = summ = role = ""
    args = myInp.split()
    if len(args) == 0:
        print("No arguments.")
        return
    name = setName(args)
    if name == None:
        return
    date = setDate(args)
    time = setTime(args)
    summ = setSumm(args)
    role = setRole(args)

    return Event(name, date, time, summ, role)


#!sch add <eventName> [OPTIONS]
#Options:
# -d <date>
# -t <time>
# -s <summary>
# -r <role>
def addEvent(myInp, myEvents):
    e = parse(myInp)
    if e is None:
        return
    for i in myEvents:
        if i.getName() == e.getName():
            print("This eventname already exists! Maybe you meant to edit?")
            return
    myEvents.append(e)

def editEvent(myInp, myEvents):
    e = parse(myInp)

while inp is not "done":
    inp = input("Enter here: ")
    addEvent(inp, myEvents)
    print(myEvents)