class Applicant(User):
    def __init__(self, fname, mname, lname, applicantID, uploadedDocuments):
        super().__init__(fname, mname, lname)
        self.applicantID = applicantID
        self.uploadedDocuments = uploadedDocuments

    def getApplicantID(self):
        return self.applicantID

    def getClassName(self):
        return "Applicant"

    def getUploadedDocuments(self):
        return self.uploadedDocuments

    def setUploadedDocument(self, newDocumentID):
        self.uploadedDocuments.append(newDocumentID)

    def __eq__(self, compare):
        return self.applicantID == compare.applicantID

