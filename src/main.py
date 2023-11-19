import os # for clearing screen
import re # for regex input validation

from peewee import *
import importlib
import Database
from Student import Student
from Faculty import Faculty
from Applicant import Applicant
importlib.reload(Database)
from Database import Database
from datetime import datetime
import easygui

# requires 'pip install prompt_toolkit'
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError # for input validation
from prompt_toolkit import prompt

# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file)
database = Database(db)

# INPUT VALIDATOR
class InputValidator(Validator):
    
    def __init__(self, numMenu=0, alphaSpace=False, num=False, yes=False, empty=True):
        self.numMenu = numMenu
        self.alphaSpace = alphaSpace
        self.num = num
        self.yes = yes
        self.empty = empty
    
    def validate(self, document: Document):
        text = document.text
        if self.empty and not text:
            raise ValidationError(message='')
        elif ((self.numMenu > 0) or self.num) and not text.isdigit():
            raise ValidationError(message='This input contains non-numeric characters')
        elif (self.numMenu > 0) and text.isdigit() and not (int(text) >= 1 and int(text) <= self.numMenu):
            raise ValidationError(message='The menu only has digits 1 to ' + str(self.numMenu) + ' as choices')
        elif self.alphaSpace and not re.match("^[a-z ]+$", text.lower()):
            raise ValidationError(message='This input contains non-alphabet/space characters')
        elif self.yes and not (text.lower()=='y' or text.lower()=='n'):
            raise ValidationError(message='Your choice are only \'Y\' and \'N\'')

def menuMain():
    choice = 0
    while not (choice > 0 and choice < 5):
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|     " + "\033[1;33m" + "ELMWOOD UNIVERSITY" + "\033[0m" + "\033[1;32m" + "     |")
        print("==============================")
        print("\033[0m")
        print("\033[1;35m" + "1 " + "\033[0m" + "Enrollment Page")
        print("\033[1;35m" + "2 " + "\033[0m" + "Login Page")
        print("\033[1;35m" + "3 " + "\033[0m" + "Exit")
        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=3)))
    return choice

def menuEnrollment():
    fname = ""
    mname = ""
    lname = ""
    email = ""
    file = None

    choice = 0
    while choice != 4:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|          ENROLLMENT        |")
        print("==============================")
        print("\033[0m")

        print()
        print("*First Name:  ", fname)
        print(" Middle Name: ", mname)
        print("*Last Name:   ", lname)
        print("*Email:       ", email)
        print(" Document:    ", file)
        print()

        print("\033[1;32m" + "1 " + "\033[0m" + "Fill-out Information")
        print("\033[1;32m" + "2 " + "\033[0m" + "Upload Documents")
        print("\033[1;32m" + "3 " + "\033[0m" + "Submit Application")
        print("\033[1;32m" + "4 " + "\033[0m" + "Back to Main Menu")

        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=4)))

        if choice == 1:  # Fill-out Information
            consoleClear()
            fname = prompt("*Enter First Name:  ", validator=InputValidator(alphaSpace=True))
            mname = prompt(" Enter Middle Name: ", validator=InputValidator(alphaSpace=True, empty=False))
            lname = prompt("*Enter Last Name:   ", validator=InputValidator(alphaSpace=True))
            email = prompt("*Enter Email:       ", validator=InputValidator())
        elif choice == 2:  # Upload Documents
            print("Selected Upload Documents")
            # Open a file dialog
            file = easygui.fileopenbox()  # show an "Open" dialog box and return the path to the selected file
        elif choice == 3:  # Submit Application
            if (fname != None) and (lname != None) and (email != None):
                database.createApplicant(fname, mname, lname, email)
                if file:
                    database.uploadDocument(email, file)
                print("Successfully submitted application!")
                choice = 4
                consolePause()
        elif choice == 4:
            pass  # Back to Main Menu
        else:
            print("\033[1;31m" + "Invalid choice. Please try again." + "\033[0m")

def menuLogin():
    email = ''
    password = ''
    role = None
    choice = 0
    while choice != 4:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|         LOGIN PAGE         |")
        print("==============================")
        print("\033[0m")

        print()
        print("Email:    ", email)
        print("Password: ", password)
        print()

        print("\033[1;35m" + "1 " + "\033[0m" + "Enter Email")
        print("\033[1;35m" + "2 " + "\033[0m" + "Enter Password")
        print("\033[1;35m" + "3 " + "\033[0m" + "Login")
        print("\033[1;35m" + "4 " + "\033[0m" + "Exit")
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=4)))

        if choice == 1:
            consoleClear()
            print("Selected Enter Email")
            email = prompt("Enter Email: ", validator=InputValidator())
        elif choice == 2:
            consoleClear()
            print("Selected Enter Password")
            password = prompt("Enter Password: ", validator=InputValidator())
        elif choice == 3:
            consoleClear()
            role = database.signIn(email, password)
            if role == "Student":
                menuStudent(email)
            elif role == "Admin":
                menuAdmin(email)
            elif role == "Faculty":
                menuFaculty(email)
            elif role == "Staff":
                menuStaff(email)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            consolePause()
            continue

def menuStudent(email):
    choice = 0
    while choice != 3:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|           STUDENT          |")
        print("==============================")
        print("\033[0m")
        print("\033[1;35m" + "1 " + "\033[0m" + "Submit Documents")
        print("\033[1;35m" + "2 " + "\033[0m" + "See Information")
        print("\033[1;35m" + "3 " + "\033[0m" + "Logout")

        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=3)))

        if choice == 1:
            print("Selected Submit Documents")
            # Open a file dialog
            file = easygui.fileopenbox() # show an "Open" dialog box and return the path to the selected file
            print(f'Document: {file}')
            confirm = prompt("Do you want to proceed? (Y/N): ", validator=InputValidator(yes=True)).lower()
            if confirm.lower() == "y":
                database.uploadDocument(email, file)
                print()
                print("Documents have been uploaded.")
            else:
                print("Cancelled uploading documents.")
            consolePause()
        elif choice == 2:
            student = database.getStudentByEmail(email)
            if student is not None:
                print(f"Student ID: {student.studentID}\nName: {student.fname} {student.mname} {student.lname}\nEmail: {student.email}\n")
                database.displayStudentGrades(student.studentID)
            else:
                print("Invalid student data.")
            consolePause()
        elif choice == 3:
            pass
        else:
            print("\033[1;31m")
            print("Invalid choice. Please try again.")
            print("\033[0m")

def menuFaculty(email):
    choice = 0
    while choice != 4:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|           FACULTY          |")
        print("==============================")
        print("\033[0m")

        print("\033[1;35m" + "1 " + "\033[0m" + "Input Student Grades")
        print("\033[1;35m" + "2 " + "\033[0m" + "Search Student Records")
        print("\033[1;35m" + "3 " + "\033[0m" + "Generate Class Report")
        print("\033[1;35m" + "4 " + "\033[0m" + "Logout")

        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=4)))

        if choice == 1:
            consoleClear()
            print("Selected Input Student Grades")
            database.displayFacultyCourses(email)
            sectionName = prompt("Enter Section Name: ", validator=InputValidator())
            section = database.getSectionByName(sectionName)
            if not section:
                print(f'Section {sectionName} does not exist.')
                consolePause()
                continue
            studentID = int(prompt("Enter Student ID to grade: ", validator=InputValidator(num=True)))
            student = database.getStudentByID(studentID)
            if not student:
                print(f'Student ID {studentID} does not exist.')
                consolePause()
                continue
            grade = int(prompt("Enter grade: ", validator=InputValidator(numMenu=100)))
            database.gradeStudent(student.studentID, section.sectionID, grade)
        elif choice == 2:
            consoleClear()
            print("Selected Search Student Records")
            database.displayFacultyCourses(email)
            studentID = int(prompt("Enter Student ID: ", validator=InputValidator(num=True)))
            student = database.getStudentByID(studentID)
            faculty = database.getFacultyByEmail(email)
            print(f'Student ID: {student.studentID}\nName: {student.fname} {student.mname} {student.lname}\nEmail: {student.email}\n')
            database.displayStudentGrades(studentID, faculty.facultyID)
            consolePause()
        elif choice == 3:
            consoleClear()
            print("Selected Generate Class Report")
            database.displayAllCourses()
            courseName = prompt("Enter Course Name: ", validator=InputValidator())
            course = database.getCourseByName(courseName)
            if not course:
                print(f'Course {courseName} does not exist.')
                consolePause()
                continue
            database.displayAllSections(courseName)
            sectionName = prompt("Enter Section Name: ", validator=InputValidator())
            section = database.getSectionByName(sectionName)
            if not section:
                print(f'Section {sectionName} does not exist.')
                consolePause()
                continue
            database.getClassReport(sectionName)
            consolePause()
            continue
        elif choice == 4:
            break
        else:
            print("\033[1;31m")
            print("Invalid choice. Please try again.")
            print("\033[0m")
            
            
def menuStaff(email):
    choice = 0
    while choice != 4:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|            STAFF           |")
        print("==============================")
        print("\033[0m")

        print("\033[1;35m" + "1 " + "\033[0m" + "Display Applicants (Enrollment)")
        print("\033[1;35m" + "2 " + "\033[0m" + "Search Student Records")
        print("\033[1;35m" + "3 " + "\033[0m" + "Generate Class Report")
        print("\033[1;35m" + "4 " + "\033[0m" + "Logout")
        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=4)))

        if choice == 1:
            app_choice = 0
            while app_choice != 3:
                consoleClear()
                database.displayAllApplicants()
                print("")
                print("\033[1;35m" + "1 " + "\033[0m" + "Approve an applicant")
                print("\033[1;35m" + "2 " + "\033[0m" + "Reject an applicant")
                print("\033[1;35m" + "3 " + "\033[0m" + "Go back to staff menu")
                app_choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=3)))
                if app_choice == 1:
                    applicantID = int(prompt("Enter the Applicant ID: ", validator=InputValidator(num=True)))
                    database.approveApplicant(applicantID)
                elif app_choice == 2:
                    applicantID = int(prompt("Enter the Applicant ID: ", validator=InputValidator(num=True)))
                    applicant = database.getApplicantByID(applicantID)
                    if not applicant:
                        print(f'Applicant {applicantID} does not exist.')
                        consolePause()
                        continue
                    confirm = prompt("Do you want to proceed? (Y/N): ", validator=InputValidator(yes=True)).lower()
                    if confirm == "y":
                        database.removeApplicant(applicantID)
                    else:
                        print("Applicant rejection cancelled.")
                elif app_choice == 3:
                    continue
                consolePause()
        elif choice == 2:
            consoleClear()
            print("Selected Search Student Records")
            studentID = int(prompt("Enter Student ID: ", validator=InputValidator(num=True)))
            student = database.getStudentByID(studentID)
            print(f'Student ID: {student.studentID}\nName: {student.fname} {student.mname} {student.lname}\nEmail: {student.email}\n')
            database.displayStudentGrades(studentID)
            database.displayStudentDocuments(studentID)
            consolePause()
        elif choice == 3:
            consoleClear()
            print("Selected Generate Class Report")
            database.displayAllCourses()
            courseName = prompt("Enter Course Name: ", validator=InputValidator())
            course = database.getCourseByName(courseName)
            if not course:
                print(f'Course {courseName} does not exist.')
                consolePause()
                continue
            database.displayAllSections(courseName)
            sectionName = prompt("Enter Section Name: ", validator=InputValidator())
            section = database.getSectionByName(sectionName)
            if not section:
                print(f'Section {sectionName} does not exist.')
                consolePause()
                continue
            database.getClassReport(sectionName)
            consolePause()
            continue
        elif choice == 4:
            break
        else:
            print("\033[1;31m")
            print("Invalid choice. Please try again.")
            print("\033[0m")


def menuAdmin(email):
    choice = 0
    while choice != 8:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|            ADMIN           |")
        print("==============================")
        print("\033[0m")

        print("\033[1;35m" + "1 " + "\033[0m" + "Create User")
        print("\033[1;35m" + "2 " + "\033[0m" + "Remove User")
        print("\033[1;35m" + "3 " + "\033[0m" + "Create Course")
        print("\033[1;35m" + "4 " + "\033[0m" + "Find Existing Course/Section")
        print("\033[1;35m" + "5 " + "\033[0m" + "Create Section")
        print("\033[1;35m" + "6 " + "\033[0m" + "Add Faculty to Section")
        print("\033[1;35m" + "7 " + "\033[0m" + "Add Student to Section")
        print("\033[1;35m" + "8 " + "\033[0m" + "Logout")

        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=8)))
        print()

        if choice == 1:
            menuCreateUser()
        elif choice == 2:
            email = prompt("Enter the email of the user to remove: ", validator=InputValidator())
            database.removeUserByEmail(email)
        elif choice == 3:
            consoleClear()
            print("Selected Create Course")
            courseName = prompt("Enter Course Name: ", validator=InputValidator())
            database.createCourse(courseName)
            print()
            print("Course has been created.")
            consolePause()
        elif choice == 4:
            database.displayAllCourses()
            break
        elif choice == 5:
            while True:
                try:
                    print("Selected Create Section")
                    database.displayAllCourses()
                    courseName = prompt("Enter the course name: ", validator=InputValidator())
                    course = database.getCourseByName(courseName)
                    if not course:
                        print(f'Course {courseName} does not exist.')
                        consolePause()
                        continue
                    sectionName = prompt("Enter the section name: ", validator=InputValidator())
                    database.createSection(sectionName, courseName)
                    print("Section has been created.")
                    consolePause()
                    break
                except ValueError as e:
                    print(e)
                    consolePause()
                    continue
                except:
                    print("Invalid input. Please try again.")
                    consolePause()
                    continue

        elif choice == 6:
            print("Selected Add Faculty to Section")
            database.displayAllCourses()
            courseName = prompt("Enter the course name: ", validator=InputValidator())
            course = database.getCourseByName(courseName)
            if not course:
                print(f'Course {courseName} does not exist.')
                consolePause()
                continue
            database.displayAllSections(courseName)
            sectionName = prompt("Enter Section Name to add Faculty to: ", validator=InputValidator())
            section = database.getSectionByName(sectionName)
            if not section:
                print(f'Section {sectionName} does not exist.')
                consolePause()
                continue
            database.displayAllFaculty()
            facultyID = int(prompt("Enter Faculty ID to add to section: ", validator=InputValidator(num=True)))
            faculty = database.getFacultyByID(facultyID)
            if not faculty:
                print(f'Faculty ID {facultyID} does not exist.')
                consolePause()
                continue
            database.addFacultyToSection(facultyID, sectionName)

        elif choice == 7:
            print("Selected Add Student to Section")
            database.displayAllCourses()
            courseName = prompt("Enter the course name: ", validator=InputValidator())
            course = database.getCourseByName(courseName)
            if not course:
                print(f'Course {courseName} does not exist.')
                consolePause()
                continue
            database.displayAllSections(courseName)
            sectionName = prompt("Enter Section Name to add Student to: ", validator=InputValidator())
            section = database.getSectionByName(sectionName)
            if not section:
                print(f'Section {sectionName} does not exist.')
                consolePause()
                continue
            database.displayAllStudents()
            studentID = int(prompt("Enter Student ID to add to section: ", validator=InputValidator(num=True)))
            student = database.getStudentByID(studentID)
            if not student:
                print(f'Student ID {studentID} does not exist.')
                consolePause()
                continue
            database.addStudentToSection(studentID, sectionName)
        elif choice == 8:
            break
        else:
            print("\033[1;31m")
            print("Invalid choice. Please try again.")
            print("\033[0m")


def menuCreateUser():
    type = ""
    choice = 0
    while choice != 5:
        consoleClear()
        print("\033[1;32m")
        print("==============================")
        print("|         CREATE USER        |")
        print("==============================")
        print("\033[0m")
        print()
        print("Select the type of user to create: ")
        print()
        print("\033[1;35m" + "1 " + "\033[0m" + "Student")
        print("\033[1;35m" + "2 " + "\033[0m" + "Faculty")
        print("\033[1;35m" + "3 " + "\033[0m" + "Staff")
        print("\033[1;35m" + "4 " + "\033[0m" + "Admin")
        print("\033[1;35m" + "5 " + "\033[0m" + "Back to Admin Menu")
        print()
        choice = int(prompt("Enter your choice: ", validator=InputValidator(numMenu=5)))
        print()

        if choice == 1:
            print("Selected Student")
            type = "Student"
        elif choice == 2:
            print("Selected Faculty")
            type = "Faculty"
        elif choice == 3:
            print("Selected Staff")
            type = "Staff"
        elif choice == 4:
            print("Selected Admin")
            type = "Admin"
        elif choice == 5:
            pass
        else:
            print("\033[1;31mInvalid choice. Please try again.\033[0m")

        if choice == 5:
            break
        elif type == "Student" or type == "Faculty" or type == "Staff":
            fname = prompt("Enter First Name:  ", validator=InputValidator(alphaSpace=True))
            mname = prompt("Enter Middle Name: ", validator=InputValidator(alphaSpace=True))
            lname = prompt("Enter Last Name:   ", validator=InputValidator(alphaSpace=True))

            if type == "Student":
                database.createStudent(fname, mname, lname)
            elif type == "Faculty":
                database.createFaculty(fname, mname, lname)
            elif type == "Staff":
                database.createStaff(fname, mname, lname)
        elif type == "Admin":
            email = prompt("Enter Email:    ", validator=InputValidator())
            password = prompt("Enter Password: ", validator=InputValidator())

            database.createAdmin(email, password)

        print()
        print("User has been created.")
        consolePause()


def consoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')

def consolePause():
    if os.name == "nt":
        print()
        os.system("pause")
    else:
        print()
        print("Press Enter to continue...")
        input()

choice = 0

while choice != 3:
    choice = menuMain()
    if choice == 1:    # Enrollment Page
        menuEnrollment()
    elif choice == 2:  # Login Page
        menuLogin()
    elif choice == 3:  # Exit
        break
    else:
        print("Invalid choice. Please try again.")