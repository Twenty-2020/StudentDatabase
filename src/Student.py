from User import User
class Student(User):
    def __init__(self, email, password, fname, mname, lname, studentID, uploadedDocuments=[]):
        super().__init__(email, password, fname, mname, lname)
        self.studentID = studentID
        self.uploadedDocuments = uploadedDocuments
        self.enrolledSections = []
        self.grades = {}

    def getStudentID(self):
        return self.studentID

    def getEnrolledSections(self):
        return self.enrolledSections

    def getUploadedDocuments(self):
        return self.uploadedDocuments

    def getGrade(self, sectionID):
        if sectionID in self.grades:
            return self.grades[sectionID]
        else:
            return 0.0

    def getClassName(self):
        return "Student"

    def setEnrolledSection(self, newSectionID):
        self.enrolledSections.append(newSectionID)

    def setUploadedDocument(self, newDocumentID):
        self.uploadedDocuments.append(newDocumentID)

    def __eq__(self, compare):
        return self.studentID == compare.studentID
