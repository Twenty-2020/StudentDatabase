import json
import tabulate
import os
import math
from typing import List
import shutil
import time
from peewee import *
from Course import Course
from Admin import Admin
from Applicant import Applicant
from Faculty import Faculty
from Staff import Staff
from Student import Student
from Section import Section
class Database:

    def __init__(self):
        self.applicants = []
        self.students = []
        self.faculty = []
        self.staff = []
        self.admins = []
        self.courses = []
        self.sections = []

    def __del__(self):
        self.applicants.clear()
        self.students.clear()
        self.faculty.clear()
        self.staff.clear()
        self.admins.clear()
        self.courses.clear()
        self.sections.clear()

    def findUserByEmail(self, email: str):
        for user in self.students:
            if user.getEmail() == email:
                return user

        for user in self.faculty:
            if user.getEmail() == email:
                return user

        for user in self.staff:
            if user.getEmail() == email:
                return user

        for user in self.admins:
            if user.getEmail() == email:
                return user

        return None # User not found.

    def findUserByEmailAndPassword(self, email: str, password: str):
        for user in self.students:
            if user.getEmail() == email and user.getPassword() == password:
                return user

        for user in self.faculty:
            if user.getEmail() == email and user.getPassword() == password:
                return user

        for user in self.staff:
            if user.getEmail() == email and user.getPassword() == password:
                return user

        for user in self.admins:
            if user.getEmail() == email and user.getPassword() == password:
                return user

        return None # User not found.

    def get_last_id(self, class_name: str) -> int:
        if class_name == "Applicant":
            if not self.applicants:
                return 0
            return self.applicants[-1].getApplicantID()
        elif class_name == "Student":
            current_year = datetime.datetime.now().year
            if not self.students:
                return current_year * 100000
            return (current_year * 100000) + (self.students[-1].getStudentID() % 100000)
        elif class_name == "Faculty":
            if not self.faculty:
                return 0
            return self.faculty[-1].getFacultyID()
        elif class_name == "Staff":
            if not self.staff:
                return 0
            return self.staff[-1].getStaffID()
        elif class_name == "Admin":
            if not self.admins:
                return 0
            return self.staff[-1].getStaffID()
        elif class_name == "Course":
            if not self.courses:
                return 0
            return self.courses[-1].getCourseID()
        elif class_name == "Section":
            current_year = datetime.datetime.now().year
            if not self.sections:
                return (current_year % 100) * 1000
            return ((current_year % 100) * 1000) + (self.sections[-1].getSectionID() % 1000)
        else:
            print("Passed className is not valid.")
        return -1

    def find_course_by_id(self, search: str) -> Course:
        for course in self.courses:
            if str(course.getCourseID()) == search:
                return course

        return None
    
    def insertApplicant(self, user: Applicant):
        self.applicants.append(user)

    def insertStudent(self, user: Student):
        self.students.append(user)

    def insertFaculty(self, user: Faculty):
        self.faculty.append(user)

    def insertStaff(self, user: Staff):
        self.staff.append(user)

    def insertAdmin(self, user: Admin):
        self.admins.append(user)

    def insertCourse(self, course: Course):
        self.courses.append(course)

    def insertSection(self, section: Section):
        self.sections.append(section)

    def removeApplicant(self, user: Applicant):
        self.applicants.remove(user)
        saveList(self.DATADIR, "applicants", self.applicants)

    def removeStudent(self, user: Student):
        self.students.remove(user)
        saveList(self.DATADIR, "students", self.students)

    def removeFaculty(self, user: Faculty):
        self.faculty.remove(user)
        saveList(self.DATADIR, "faculty", self.faculty)

    def removeStaff(self, user: Staff):
        self.staff.remove(user)
        saveList(self.DATADIR, "staff", self.staff)

    def removeAdmin(self, user: Admin):
        self.admins.remove(user)
        saveList(self.DATADIR, "admins", self.admins)

    def removeCourse(self, course: Course):
        self.courses.remove(course)
        saveList(self.DATADIR, "courses", self.courses)

    def removeSection(self, section: Section):
        self.sections.remove(section)
        saveList(self.DATADIR, "sections", self.sections)

    def printListApplicants(self):
        table = tabulate.Table()
        table.format().width(20).corner(" ").corner_color(tabulate.Color.cyan)
        table.add_row(["Applicant ID", "First Name", "Middle Name", "Last Name"])
        for user in self.applicants:
            table.add_row([str(user.getApplicantID()), user.getFName(), user.getMName(), user.getLName()])
        print(table)

    def printListStudents(self):
        pass

    def printListFaculty(self):
        pass
    def printListStaff(self):
        pass

    def printListAdmin(self):
        pass

    def printListCourse(self):
        pass

    def printListSection(self):
        pass

    def printListSectionByCourse(self, course):
       pass

    def printClassReport(self, section):
        pass

    def saveList(self, dataDir, fileName, dataList):
        listJson = json.dumps(dataList)
        with open(dataDir + fileName + ".json", "w") as listFile:
            listFile.write(listJson)

    def saveDatabase(self, dataDir):
        self.saveList(dataDir, "applicants", self.applicants)
        self.saveList(dataDir, "students", self.students)
        self.saveList(dataDir, "faculty", self.faculty)
        self.saveList(dataDir, "staff", self.staff)
        self.saveList(dataDir, "admins", self.admins)
        self.saveList(dataDir, "courses", self.courses)
        self.saveList(dataDir, "sections", self.sections)


    def loadList(dataDir, fileName, dataList):
        try:
            # Load JSON file into the corresponding list
            with open(dataDir + fileName + ".json", "r") as listFile:
                listJson = json.load(listFile)

            # Deserialize JSON into list
            dataList = listJson

            # Close the file
            listFile.close()
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            print("JSON parsing error: ", e)

    def loadDatabase(dataDir):
        loadList(dataDir, "applicants", applicants)
        loadList(dataDir, "students", students)
        loadList(dataDir, "faculty", faculty)
        loadList(dataDir, "staff", staff)
        loadList(dataDir, "admins", admins)
        loadList(dataDir, "courses", courses)
        loadList(dataDir, "sections", sections)

    # OTHER METHODS

    def newApplicant(fname, mname, lname, uploadedDocuments):
        applicantID = getLastID("Applicant") + 1
        
        insertApplicant(Applicant(fname, mname, lname, applicantID, uploadedDocuments))
        saveList(DATADIR, "applicants", applicants)

    def approveApplicant(user):
        fname = user.getFName()
        mname = user.getMName()
        lname = user.getLName()
        uploadedDocuments = user.getUploadedDocuments()
        studentID = getLastID("Student") + 1
        email = str(studentID) + "@elmwood.edu.ph"
        password = lname + str(studentID)
        
        insertStudent(Student(email, password, fname, mname, lname, studentID, uploadedDocuments))
        removeApplicant(user)
        saveList(DATADIR, "applicants", applicants)
        saveList(DATADIR, "students", students)

    def createStudent(fname, mname, lname):
        studentID = getLastID("Student") + 1
        email = str(studentID) + "@elmwood.edu.ph"
        password = lname + str(studentID)
        
        insertStudent(Student(email, password, fname, mname, lname, studentID))
        saveList(DATADIR, "students", students)

    def createFaculty(fname, mname, lname):
        facultyID = getLastID("Faculty") + 1
        email = "faculty" + str(facultyID) + "@elmwood.edu.ph"
        password = lname + str(facultyID)
        
        insertFaculty(Faculty(email, password, fname, mname, lname, facultyID))
        saveList(DATADIR, "faculty", faculty)

    def createStaff(fname, mname, lname):
        staffID = getLastID("Staff") + 1
        email = "staff" + str(staffID) + "@elmwood.edu.ph"
        password = lname + str(staffID)
        
        insertStaff(Staff(email, password, fname, mname, lname, staffID))
        saveList(DATADIR, "staff", staff)

    def createAdmin(email, password):
        adminID = getLastID("Admin") + 1
        
        insertAdmin(Admin(email, password, adminID))
        saveList(DATADIR, "admins", admins)

    def createCourse(courseName):
        courseID = getLastID("Course") + 1
        insertCourse(Course(courseID, courseName))
        saveList(DATADIR, "courses", courses)

    def createSection(courseID, sectionName):
        sectionID = getLastID("Section") + 1
        insertSection(Section(courseID, sectionID, sectionName, 0))
        course = findCourseByID(str(courseID))
        if course:
            course.addSection(sectionID)
            saveList(DATADIR, "sections", sections)

    def findSectionByID(sectionID):
        for section in sections:
            if section.getSectionID() == sectionID:
                return section
        return None

    def findStudentByID(studentID):
        for student in students:
            if student.getStudentID() == studentID:
                return student
        return None

    def findApplicantByID(applicantID):
        for applicant in applicants:
            if applicant.getApplicantID() == applicantID:
                return applicant
        return None

    def findFacultyByID(facultyID):
        for user in faculty:
            if user.getFacultyID() == facultyID:
                return user
        return None

    def addFacultyToSection(section, user):
        sectionID = section.getSectionID()
        facultyID = user.getFacultyID()

        section.setAssignedFaculty(facultyID)
        user.setAssignedSection(sectionID)

        saveList(DATADIR, "sections", sections)
        saveList(DATADIR, "faculty", faculty)

    def addStudentToSection(section, user):
        sectionID = section.getSectionID()
        studentID = user.getStudentID()

        section.addEnrolledStudent(studentID)
        user.setEnrolledSection(sectionID)

        saveList(DATADIR, "sections", sections)
        saveList(DATADIR, "students", students)

    def checkFacultyInSection(email, section):
        user = findUserByEmail(email)
        sectionID = section.getSectionID()
        if user:
            faculty = isinstance(user, Faculty)
            assignedSections = faculty.getAssignedSections()
            for assignedSectionID in assignedSections:
                if assignedSectionID == sectionID:
                    return True
        return False
    
    def uploadDocument(email):
        # Get the current timestamp in nanoseconds
        timestamp = str(int(time.time() * 1e9))

        # Create a directory with the timestamp in "../data/uploads"
        datadir = os.environ.get('DATADIR')
        uploadDir = os.path.join(datadir, "uploads", timestamp)
        os.makedirs(uploadDir)

        # Copy documents from "../external" to the new folder
        externalDir = os.environ.get('EXTDIR')
        for entry in os.scandir(externalDir):
            sourcePath = entry.path
            sourceName = entry.name
            shutil.copy(sourcePath, os.path.join(uploadDir, sourceName))

        # Check if user is an Applicant or Student then set the uploadedDocument
        user = findUserByEmail(email)
        if user and user.getClassName() == "Student":
            student = user
            student.setUploadedDocument(timestamp)
            saveList(os.environ.get('DATADIR'), "students", students)
            print("Document has been uploaded to", uploadDir)
        return timestamp
