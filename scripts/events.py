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
            toRet = toRet + "\n--Role: \\" + self.role
        return toRet + "\n"

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_role(self):
        return self.role

    def get_summ(self):
        return self.summ

    def set_name(self, name):
        self.name = name
    
    def set_date(self, date):
        self.date = date
    
    def set_time(self, time):
        self.time = time
    
    def set_role(self, role):
        self.role = role
 
    def set_summ(self, summ):
        self.summ = summ