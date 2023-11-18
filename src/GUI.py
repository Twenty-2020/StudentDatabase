'''
    This file contains the GUI for the Elmwood University application.
    Basic Tkinter implementation
'''
import tkinter as tk
from tkinter import ttk, messagebox
from peewee import SqliteDatabase

# Tkinter GUI for the main application
class ElmwoodUniversityApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Elmwood University")
        self.master.geometry("400x300")

        self.label = tk.Label(master, text="ELMWOOD UNIVERSITY", font=("Arial", 16))
        self.label.pack(pady=20)

        self.enrollment_button = tk.Button(master, text="Enrollment Page", command=self.enrollment_page)
        self.enrollment_button.pack(pady=10)

        self.login_button = tk.Button(master, text="Login Page", command=self.login_page)
        self.login_button.pack(pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=10)

    def enrollment_page(self):
        enrollment_root = tk.Toplevel(self.master)
        enrollment_app = EnrollmentApp(enrollment_root)

    def login_page(self):
        login_root = tk.Toplevel(self.master)
        login_app = LoginPage(login_root)

    def exit_program(self):
        self.master.destroy()
    
# Tkinter GUI for the enrollment page
class EnrollmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enrollment")

        self.fname_var = tk.StringVar()
        self.mname_var = tk.StringVar()
        self.lname_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for user input
        ttk.Label(self.root, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.root, textvariable=self.fname_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Middle Name:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.root, textvariable=self.mname_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Last Name:").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.root, textvariable=self.lname_var).grid(row=2, column=1, padx=5, pady=5)

        # Buttons for actions
        ttk.Button(self.root, text="Fill-out Information", command=self.fill_out_info).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Upload Documents", command=self.upload_documents).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Submit Application", command=self.submit_application).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Back to Main Menu", command=self.root.destroy).grid(row=6, column=0, columnspan=2, pady=10)

    def fill_out_info(self):
        messagebox.showinfo("Information", "Fill-out Information button clicked!")

    def upload_documents(self):
        messagebox.showinfo("Information", "Upload Documents button clicked!")

    def submit_application(self):
        # Placeholder for the actual submission logic
        messagebox.showinfo("Information", "Successfully submitted application!")

# Tkinter GUI for the login page
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Email:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.root, textvariable=self.email_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.root, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.root, text="Enter Email", command=self.enter_email).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Enter Password", command=self.enter_password).grid(row=3, column=0, columnspan=2, pady=10)

    def enter_email(self):
        print("Entered Email:", self.email_var.get())

    def enter_password(self):
        print("Entered Password:", self.password_var.get())

# Tkinter GUI for the student menu
class StudentMenu:
    def __init__(self, root, email):
        self.root = root
        self.root.title("Student Menu")
        self.email = email

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="STUDENT", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Submit Documents", command=self.submit_documents).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="See Information", command=self.see_information).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Logout", command=self.logout).grid(row=3, column=0, columnspan=2, pady=10)

    def submit_documents(self):
        print("Selected Submit Documents")
        confirm = tk.messagebox.askquestion("Confirmation", "All files in 'external/' folder will be uploaded. Do you want to proceed?")
        if confirm == "yes":
            # Implement document submission logic
            print("Documents have been uploaded.")
        else:
            print("Cancelled uploading documents.")

    def see_information(self):
        # Implement logic to see student information
        print("See Information")

    def logout(self):
        # Implement logout logic
        print("Logout")

# Tkinter GUI for the Faculty menu
class FacultyMenu:
    def __init__(self, root, email):
        self.root = root
        self.root.title("Faculty Menu")
        self.email = email

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="FACULTY", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Input Student Grades", command=self.input_student_grades).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Search Student Records", command=self.search_student_records).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Generate Class Report", command=self.generate_class_report).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=2, pady=10)

    def input_student_grades(self):
        # Implement logic for inputting student grades
        print("Selected Input Student Grades")

    def search_student_records(self):
        # Implement logic for searching student records
        print("Selected Search Student Records")

    def generate_class_report(self):
        # Implement logic for generating class report
        print("Selected Generate Class Report")

    def logout(self):
        # Implement logout logic
        print("Logout")

# Tkinter GUI for the Staff menu
class StaffMenu:
    def __init__(self, root, email):
        self.root = root
        self.root.title("Staff Menu")
        self.email = email

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="STAFF", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Display Applicants", command=self.display_applicants).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Search Student Records", command=self.search_student_records).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Generate Class/Course Report", command=self.generate_report).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=2, pady=10)

    def display_applicants(self):
        # Implement logic for displaying applicants
        print("Selected Display Applicants")

    def search_student_records(self):
        # Implement logic for searching student records
        print("Selected Search Student Records")

    def generate_report(self):
        # Implement logic for generating class/course report
        print("Selected Generate Class/Course Report")

    def logout(self):
        # Implement logout logic
        print("Logout")

# Tkinter GUI for the Admin menu
class AdminMenu:
    def __init__(self, root, email):
        self.root = root
        self.root.title("Admin Menu")
        self.email = email

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="ADMIN", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Create User", command=self.create_user).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Remove User", command=self.remove_user).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Create Course", command=self.create_course).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Find Existing Course/Section", command=self.find_course_section).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Create Section", command=self.create_section).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Add Faculty to Section", command=self.add_faculty_to_section).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Add Student to Section", command=self.add_student_to_section).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Logout", command=self.logout).grid(row=8, column=0, columnspan=2, pady=10)

    def create_user(self):
        # Implement logic for creating a user
        print("Selected Create User")

    def remove_user(self):
        # Implement logic for removing a user
        print("Selected Remove User")

    def create_course(self):
        # Implement logic for creating a course
        print("Selected Create Course")

    def find_course_section(self):
        # Implement logic for finding an existing course/section
        print("Selected Find Existing Course/Section")

    def create_section(self):
        # Implement logic for creating a section
        print("Selected Create Section")

    def add_faculty_to_section(self):
        # Implement logic for adding faculty to a section
        print("Selected Add Faculty to Section")

    def add_student_to_section(self):
        # Implement logic for adding student to a section
        print("Selected Add Student to Section")

    def logout(self):
        # Implement logout logic
        print("Logout")

# Tkinter GUI for the Create User menu
class CreateUserMenu:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Create User")
        self.db = db

        self.type_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="CREATE USER", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Radiobutton(self.root, text="Student", variable=self.type_var, value="Student").grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Radiobutton(self.root, text="Faculty", variable=self.type_var, value="Faculty").grid(row=2, column=0, columnspan=2, pady=5)
        ttk.Radiobutton(self.root, text="Staff", variable=self.type_var, value="Staff").grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Radiobutton(self.root, text="Admin", variable=self.type_var, value="Admin").grid(row=4, column=0, columnspan=2, pady=5)

        ttk.Button(self.root, text="Create User", command=self.create_user).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Back to Admin Menu", command=self.root.destroy).grid(row=6, column=0, columnspan=2, pady=10)

    def create_user(self):
        user_type = self.type_var.get()
        
        if user_type in ["Student", "Faculty", "Staff"]:
            fname = input("Enter First Name: ")
            mname = input("Enter Middle Name: ")
            lname = input("Enter Last Name: ")

            if user_type == "Student":
                self.db.createStudent(fname, mname, lname)
            elif user_type == "Faculty":
                self.db.createFaculty(fname, mname, lname)
            elif user_type == "Staff":
                self.db.createStaff(fname, mname, lname)

        elif user_type == "Admin":
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            self.db.createAdmin(email, password)

        print("User has been created.")

# Tkinter GUI for the main application
class MainApp:
    def __init__(self, root, db):
        self.root = root
        self.db = db

        self.root.title("Elmwood University")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="ELMWOOD UNIVERSITY", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Enrollment Page", command=self.menu_enrollment).grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Button(self.root, text="Login Page", command=self.menu_login).grid(row=2, column=0, columnspan=2, pady=5)
        ttk.Button(self.root, text="Exit", command=self.exit_program).grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Button(self.root, text="Faculty Menu", command=self.menu_faculty).grid(row=4, column=0, columnspan=2, pady=5)

    def menu_enrollment(self):
        enrollment_root = tk.Toplevel(self.root)
        enrollment_app = EnrollmentApp(enrollment_root)

    def menu_login(self):
        login_root = tk.Toplevel(self.root)
        login_app = LoginPage(login_root)

    def exit_program(self):
        self.db.saveDatabase("../data/")
        self.root.destroy()

    def menu_faculty(self):
        # Implement your faculty menu logic here
        print("Faculty Menu")

    def console_pause(self):
        popup = tk.Toplevel(self.root)
        popup.title("Press any key to continue...")
        ttk.Label(popup, text="Press any key to continue...").pack(pady=10)
        popup.bind("<Any-KeyPress>", lambda event: popup.destroy())

def console_pause(self):
        popup = tk.Toplevel(self.root)
        popup.title("Press any key to continue...")
        ttk.Label(popup, text="Press any key to continue...").pack(pady=10)
        popup.bind("<Any-KeyPress>", lambda event: popup.destroy())

if __name__ == "__main__":
    root = tk.Tk()
    db = SqliteDatabase('studentdatabase.db')
    app = ElmwoodUniversityApp(root, db)
    root.mainloop()
