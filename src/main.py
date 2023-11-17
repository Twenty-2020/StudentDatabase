import os
import sys
from Database import Database




db = Database()

# Load the latest database files
#db.loadDatabase("../data/")


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
    print("\033[1;34m" + "Enter your choice: " + "\033[0m")
    choice = int(input())
    input()
  return choice
match = 1
db.printListSectionByCourse(match)

def menuEnrollment():
  fname = ""
  mname = ""
  lname = ""
  uploadedDocuments = []
  
  choice = 0
  while choice != 4:
    consoleClear()
    print("\033[1;32m")
    print("==============================")
    print("|          ENROLLMENT        |")
    print("==============================")
    print("\033[0m")
  
    print()
    print("First Name:  ", fname)
    print("Middle Name: ", mname)
    print("Last Name:   ", lname)
    print()
  
    print("\033[1;32m" + "1 " + "\033[0m" + "Fill-out Information")
    print("\033[1;32m" + "2 " + "\033[0m" + "Upload Documents")
    print("\033[1;32m" + "3 " + "\033[0m" + "Submit Application")
    print("\033[1;32m" + "4 " + "\033[0m" + "Back to Main Menu")
  
    print()
    print("\033[1;34m" + "Enter your choice: " + "\033[0m")
    choice = int(input())
    input()

    if choice == 1: # Fill-out Information
      consoleClear()
      print("Enter First Name:  ")
      fname = input()
      print("Enter Middle Name: ")
      mname = input()
      print("Enter Last Name:   ")
      lname = input()
    elif choice == 2: # Upload Documents
      print("Selected Upload Documents")
      print("All files in \"external/\" folder will be uploaded.")
      confirm = input("Do you want to proceed? (Y/N): ")
      if confirm == "y" or confirm == "Y":
        #documentTimestamp = db.uploadDocument("Applicant")
        uploadedDocuments.append(documentTimestamp)
      else:
        print("Cancelled uploading documents.")
      consolePause()
    elif choice == 3: # Submit Application
      #db.newApplicant(fname, mname, lname, uploadedDocuments)
      print("Successfully submitted application!")
      choice = 4
      consolePause()
    elif choice == 4: # Back to Main Menu
      pass
    else:
      print("\033[1;31m" + "Invalid choice. Please try again." + "\033[0m")
  
def menuLogin():
  email = ""
  password = ""
  user = None
    
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
      
    print("1. Enter Email")
    print("2. Enter Password")

def menuStudent(email):
  pass

def menuFaculty(email):
  pass

def menuStaff(email):
  pass

def menuAdmin(email):
  pass

def menuCreateUser():
  pass


def menuStudent(email):
  choice = 0
  while choice != 3:
    consoleClear()
    print("\033[1;32m")
    print("==============================")
    print("|           STUDENT          |")
    print("==============================")
    print("\033[0m")

    print("1. Submit Documents")
    print("2. See Information")
    print("3. Logout")

    print()
    print("\033[1;34m", end="")
    choice = int(input("Enter your choice: "))
    print("\033[0m")
    input()

    if choice == 1:
      print("Selected Submit Documents")
      print("All files in \"external/\" folder will be uploaded.")
      confirm = input("Do you want to proceed? (Y/N): ")
      input()
      if confirm.lower() == "y":
        db.uploadDocument(email)
        print()
        print("Documents have been uploaded.")
      else:
        print("Cancelled uploading documents.")

      consolePause()
    elif choice == 2:
      user = db.findUserByEmail(email)

      if user and user.getClassName() == "Student":
        student = user

        print("Student ID: ", student.getStudentID())
        print("Full Name: ", student.getFullName())

        assignedSections = student.getEnrolledSections()
        print("Assigned Sections:")
        for sectionID in assignedSections:
          section = db.findSectionByID(sectionID)
          if section:
            print("  - Section Name: ", section.getSectionName())

            grade = student.getGrade(sectionID)
            print("    Grade: ", grade)
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

    print("1. Input Student Grades")
    print("2. Search Student Records")
    print("3. Generate Class Report")
    print("4. Logout")

    print()
    print("\033[1;34m", end="")
    print("Enter your choice: ", end="")
    print("\033[0m", end="")
    choice = int(input())
    input().strip()

    if choice == 1:
      sectionID, studentID, grade = 0, 0, 0.0
      print("Selected Input Student Grades")
      match = db.findUserByEmail(email)
      if match:
        faculty = match
        if isinstance(faculty, Faculty):
          # Display the assigned sections
          assignedSections = faculty.getAssignedSections()
          print("Assigned Sections")
          for sections in assignedSections:
            print("Sections: ", sections)
          print("Enter the Section ID to Grade: ", end="")
          sectionID = int(input())
          input().strip()

          # Display enrolled students in section
          sectionMatch = db.findSectionByID(sectionID)
          if sectionMatch:
            section = sectionMatch
            # Check if faculty is assigned to that section or not
            assigned = db.checkFacultyInSection(email, section)
            if assigned:
              print("Students")
              enrolledStudentIDs = section.getEnrolledStudentIDs()
              for students in enrolledStudentIDs:
                print("Students: ", students)
              print("Enter the Student ID to Grade: ", end="")
              studentID = int(input())
              input().strip()

              # Search for the student using the ID
              studentMatch = db.findStudentByID(studentID)
              if studentMatch:
                student = studentMatch
                if studentMatch:
                  print("Input the grade: ", end="")
                  grade = float(input())
                  input().strip()
                  faculty.setStudentGrade(student, section.getSectionID(), grade)
                  print("Grade: ", student.getGrade(section.getSectionID()))
                  db.saveDatabase("../data/")
              else:
                print("No student with the inputted ID has been found.")
                continue
        consolePause()
    elif choice == 2:
      email = ""
      print("Enter student email: ", end="")
      email = input()
      input().strip()
      match = db.findUserByEmail(email)
      if match:
        student = match
        print("StudentID: ", student.getStudentID(), "Name: ", student.getFullName())
      consolePause()
    elif choice == 3:
      while True:
        print("Selected Generate Class Report")
        print("Enter Section ID to generate class report for: ", end="")
        sectionID = int(input())
        input().strip()
        section = db.findSectionByID(sectionID)

        if section:
          # Check if faculty is assigned to that section or not
          assigned = db.checkFacultyInSection(email, section)
          if assigned:
            db.printClassReport(section)
          else:
            print("Cannot access section that is not assigned to faculty")
        else:
          print("Section not found.")
          consolePause()
          continue

        consolePause()
        break
    elif choice == 4:
      break
    else:
      print("\033[1;31m", end="")
      print("Invalid choice. Please try again.")
      print("\033[0m", end="")

def menuStaff(email):
  choice = 0
  while choice != 4:
    consoleClear()
    print("\033[1;32m")
    print("==============================")
    print("|            STAFF           |")
    print("==============================")
    print("\033[0m")

    print("1. Display Applicants (Enrollment)")
    print("2. Search Student Records")
    print("3. Generate Class/Course Report")
    print("4. Logout")

    print()
    print("\033[1;34m", end="")
    choice = int(input("Enter your choice: "))
    print("\033[0m")
    if choice == 1:
      while True:
        consoleClear()
        applicantID = int(input("Enter the Applicant ID: "))
        match = db.findApplicantByID(applicantID)
        if match:
          applicant = dynamic_cast[Applicant](match)
          if applicant:
            db.approveApplicant(applicant)
            print("Applicant Approved!")
        else:
          print("Applicant Not Found! Please try again.")
        break
    elif choice == 2:
      match = input("Enter student email: ")
      user = db.findUserByEmail(match)
      if user and user.getClassName() == "Student":
        student = dynamic_cast[Student](user)
        print("Student ID: ", student.getStudentID())
        print("Full Name: ", student.getFullName())
        assignedSections = student.getEnrolledSections()
        for sectionID in assignedSections:
          section = db.findSectionByID(sectionID)
          if section:
            print("Section Name: ", section.getSectionName())
            grade = student.getGrade(sectionID)
            print("Grade: ", grade)
        consolePause()
      else:
        print("No student with the inputted email found.")
        consolePause()
        continue
    elif choice == 3:
      while True:
        consoleClear()
        print("Selected Generate Class Report")
        sectionID = int(input("Enter Section ID to generate class report for: "))
        section = db.findSectionByID(sectionID)
        if section:
          db.printClassReport(section)
        else:
          print("Section not found.")
          consolePause()
          continue
        consolePause()
        break
    elif choice == 6:
      courseID = input("Enter the course: ")
      match = db.findCourseByID(courseID)
      if match:
        print()
        print("Course ", courseID, " has been found.")
        print("Course Name: ", match.getCourseName())
        print()
        print("Sections in this Course:")
        
        consolePause()
        sectionID = int(input("Enter the section: "))
        sectionMatch = db.findSectionByID(sectionID)
        if sectionMatch:
          email = input("Enter the faculty email: ")
          userMatch = db.findUserByEmail(email)
          if userMatch:
            faculty = dynamic_cast[Faculty](userMatch)
            faculty.setAssignedSection(sectionMatch.getSectionID())
        break
      else:
        print()
        print("No match has been found.")
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

    print("1. Create User")
    print("2. Remove User")
    print("3. Create Course")
    print("4. Find Existing Course/Section")
    print("5. Create Section")
    print("6. Add Faculty to Section")
    print("7. Add Student to Section")
    print("8. Logout")

    print()
    print("\033[1;34m", end="")
    print("Enter your choice: ", end="")
    choice = int(input())
    input()
    print()

    if choice == 1:
      menuCreateUser()
    elif choice == 2:
      consoleClear()
      print("Selected Remove User")
      search = input("Enter the email of the user to remove: ")
      match = db.findUserByEmail(search)
      if match:
        print()
        print(f"User {search} has been found.")
        print("User Name: ", match.getFullName())
        print()
        confirm = input("Are you sure you want to remove this user? (Y/N): ")
        if confirm == "y" or confirm == "Y":
          if isinstance(match, Student):
            db.removeStudent(match)
          elif isinstance(match, Faculty):
            db.removeFaculty(match)
          elif isinstance(match, Staff):
            db.removeStaff(match)
          elif isinstance(match, Admin):
            db.removeAdmin(match)
          print()
          print("User has been removed.")
        else:
          print("User removal cancelled.")
        consolePause()
        continue
      else:
        print()
        print("No match has been found.")
        consolePause()
        continue

      consolePause()
    elif choice == 3:
      consoleClear()
      print("Selected Create Course")
      courseName = input("Enter Course Name: ")
      db.createCourse(courseName)
      print()
      print("Course has been created.")
      consolePause()
    elif choice == 4:
      while True:
        consoleClear()
        print("Selected Find Existing Course")
        search = input("Search For Existing Course (0 to exit): ")
        if search == "0":
          break
        match = db.findCourseByID(search)
        if match:
          print()
          print(f"Course {search} has been found.")
          print("Course Name: ", match.getCourseName())
          print()
          print("Sections in this Course:")
          db.printListSectionByCourse(match)
          consolePause()
          break
        else:
          print()
          print("No match has been found.")
          consolePause()
          continue
    elif choice == 5:
      while True:
        print("Selected Create Section")
        search = input("Search For Existing Course (0 to exit): ")
        if search == "0":
          break
        match = db.findCourseByID(search)
        if match:
          courseID = match.getCourseID()
        else:
          print()
          print("No match has been found.")
          consolePause()
          continue
        print()
        print(f"Course {search} has been found.")
        print("Course Name: ", match.getCourseName())

        sectionName = input("Enter Section Name (0 to exit): ")
        if sectionName == "0":
          break

        db.createSection(courseID, sectionName)

        print()
        print("Course has been created.")
        consolePause()
        break
    elif choice == 6:
      sectionID = int(input("Enter Section ID to add faculty to: "))
      section = db.findSectionByID(sectionID)
      if section:
        print()
        print(f"Section {sectionID} has been found.")
        print("Section Name: ", section.getSectionName())
        print()
        facultyID = int(input("Enter the faculty ID to assign to the section: "))
        user = db.findFacultyByID(facultyID)
        if user:
          print()
          print(f"Faculty {facultyID} has been found.")
          print("Faculty Name: ", user.getFullName())
          print()
          confirm = input("Are you sure you want to add this faculty? (Y/N): ")
          if confirm == "y" or confirm == "Y":
            db.addFacultyToSection(section, user)
          else:
            print("Cancelled adding faculty to section.")
          consolePause()
          break
        else:
          print()
          print("No faculty with the inputted ID has been found.")
          consolePause()
          continue
        consolePause()
      else:
        print()
        print("No section with the inputted ID has been found.")
        consolePause()
        continue
    elif choice == 7:
      sectionID = int(input("Enter Section ID to enroll student to: "))
      section = db.findSectionByID(sectionID)
      if section:
        print()
        print(f"Section {sectionID} has been found.")
        print("Section Name: ", section.getSectionName())
        print()
        studentID = int(input("Enter the student ID to add to the section: "))
        user = db.findStudentByID(studentID)
        if user:
          print()
          print(f"Student {studentID} has been found.")
          print("Student Name: ", user.getFullName())
          print()
          confirm = input("Are you sure you want to enroll this student? (Y/N): ")
          if confirm == "y" or confirm == "Y":
            db.addStudentToSection(section, user)
          else:
            print("Cancelled adding faculty to section.")
          consolePause()
          break
        else:
          print()
          print("No faculty with the inputted ID has been found.")
          consolePause()
          continue
        consolePause()
      else:
        print()
        print("No section with the inputted ID has been found.")
        consolePause()
        continue
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
    print("1. Student")
    print("2. Faculty")
    print("3. Staff")
    print("4. Admin")
    print("5. Back to Admin Menu")
    print()
    print("\033[1;34mEnter your choice: \033[0m")
    choice = int(input())
    input()
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

    dataDir = "data/"
    if choice == 5:
      break
    elif type == "Student" or type == "Faculty" or type == "Staff":
      fname = ""
      mname = ""
      lname = ""
      print("Enter First Name:  ", end="")
      fname = input()
      print("Enter Middle Name: ", end="")
      mname = input()
      print("Enter Last Name:   ", end="")
      lname = input()

      if type == "Student":
        db.createStudent(fname, mname, lname)
      elif type == "Faculty":
        db.createFaculty(fname, mname, lname)
      elif type == "Staff":
        db.createStaff(fname, mname, lname)
    elif type == "Admin":
      email = ""
      password = ""
      print("Enter Email:    ", end="")
      email = input()
      print("Enter Password: ", end="")
      password = input()

      db.createAdmin(email, password)

    print()
    print("User has been created.")
    consolePause()

def consoleClear():
  if os.name == "nt":
    os.system("cls") # For Windows
  else:
    os.system("clear") # For POSIX systems

def consolePause():
  if os.name == "nt":
    print()
    print("Press any key to continue...")
    os.system("pause")
  else:
    print()
    print("Press Enter to continue...")
    input()

choice = 0

while choice != 3:
  choice = menuMain()
  if choice == 1: # Enrollment Page
    menuEnrollment()
  elif choice == 2: # Login Page
    menuLogin()
  elif choice == 3: # Exit
    db.saveDatabase("../data/")
    del db
    break
  elif choice == 4:
    menuFaculty("testemail")
  else:
    print("Invalid choice. Please try again.")