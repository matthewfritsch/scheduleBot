class Event:
    def __init__(self, name, date_time, summ, role):
        self.name = name
        self.date_time = date_time
        self.role = role
        self.summ = summ

    def __repr__(self):
        toRet = "Event: \n--Name: " + self.name
        if self.date_time is not None:
            toRet = toRet + "\n--Date: " + self.date
        if self.summ is not None:
            toRet = toRet + "\n--Summ: " + self.summ
        if self.role is not None:
            toRet = toRet + "\n--Role: \\" + self.role
        return toRet + "\n"

    def get_name(self):
        return self.name

    def get_date_time(self):
        return self.date_time

    def get_role(self):
        return self.role

    def get_summ(self):
        return self.summ

    def set_name(self, name):
        self.name = name

    def set_date_time(self, date_time):
        self.date_time = date_time

    def set_role(self, role):
        self.role = role
 
    def set_summ(self, summ):
        self.summ = summ