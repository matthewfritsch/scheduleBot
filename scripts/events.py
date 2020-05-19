class Event:
    def __init__(self, name, date_time, summary, role):
        self.name = name
        self.date_time = date_time
        self.role = role
        self.summary = summary

    def __repr__(self):
        toRet = "Event: \n--Name: " + self.name
        if self.date_time is not None:
            toRet = toRet + "\n--Date: " + self.date
        if self.summary is not None:
            toRet = toRet + "\n--Summ: " + self.summary
        if self.role is not None:
            toRet = toRet + "\n--Role: \\" + self.role
        return toRet + "\n"

    def get_name(self):
        return self.name

    def get_date_time(self):
        return self.date_time

    def get_role(self):
        return self.role

    def get_summary(self):
        return self.summary

    def set_name(self, name):
        self.name = name

    def set_date_time(self, date_time):
        self.date_time = date_time

    def set_role(self, role):
        self.role = role
 
    def set_summary(self, summary):
        self.summary = summary
