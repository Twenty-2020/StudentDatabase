class Course:
    def __init__(self, courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName
        self.sectionIDs = []

    def getCourseID(self):
        return self.courseID

    def getCourseName(self):
        return self.courseName

    def getSectionIDs(self):
        return self.sectionIDs

    def setCourseName(self, newCourseName):
        self.courseName = newCourseName

    def addSection(self, sectionID):
        self.sectionIDs.append(sectionID)

    def __eq__(self, compare):
        return self.courseID == compare.courseID
