
class Faculty(User):
    def __init__(self, email, password, fname, mname, lname, facultyID):
        super().__init__(email, password, fname, mname, lname)
        self.facultyID = facultyID
        self.assignedSections = []

    def getFacultyID(self):
        return self.facultyID

    def getAssignedSections(self):
        return self.assignedSections

    def setAssignedSection(self, newSectionID):
        self.assignedSections.append(newSectionID)

    def getClassName(self):
        return "Faculty"

    def setStudentGrade(self, student, sectionID, newGrade):
        student.grades[sectionID] = newGrade

    def __eq__(self, compare):
        return self.facultyID == compare.facultyID
