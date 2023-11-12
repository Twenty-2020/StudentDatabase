
from User import User

class Staff(User):
    def __init__(self, email, password, fname, mname, lname, staffID):
        super().__init__(email, password, fname, mname, lname)
        self.staffID = staffID

    def getStaffID(self):
        return self.staffID

    def getClassName(self):
        return "Staff"

    def __eq__(self, compare):
        return self.staffID == compare.staffID
