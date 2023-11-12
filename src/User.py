
class User:
    def __init__(self, email, password, fname=None, mname=None, lname=None):
        self.email = email
        self.password = password
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getFName(self):
        return self.fname

    def getMName(self):
        return self.mname

    def getLName(self):
        return self.lname

    def getFullName(self):
        return f"{self.lname}, {self.fname} {self.mname}" if self.mname else f"{self.lname}, {self.fname}"

    def getClassName(self):
        return "User"

    def setPassword(self, newPassword):
        self.password = newPassword
