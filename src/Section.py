class Section:
    def __init__(self, courseID, sectionID, sectionName, assignedFacultyID):
        self.courseID = courseID
        self.sectionID = sectionID
        self.sectionName = sectionName
        self.assignedFacultyID = assignedFacultyID
        self.enrolledStudentIDs = []

    # GETTER METHODS
    def getCourseID(self):
        return self.courseID

    def getSectionID(self):
        return self.sectionID

    def getSectionName(self):
        return self.sectionName

    def getAssignedFacultyID(self):
        return self.assignedFacultyID

    def getEnrolledStudentIDs(self):
        return self.enrolledStudentIDs

    # SETTER METHODS
    def setSectionName(self, newSectionName):
        self.sectionName = newSectionName

    def setAssignedFaculty(self, newFacultyID):
        self.assignedFacultyID = newFacultyID

    def addEnrolledStudent(self, studentID):
        self.enrolledStudentIDs.append(studentID)

    def removeEnrolledStudent(self, studentID):
        self.enrolledStudentIDs.remove(studentID)

    def __eq__(self, compare):
        return self.sectionID == compare.sectionID

