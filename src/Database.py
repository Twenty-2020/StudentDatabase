from typing import List
from peewee import *
from Course import Course
from Admin import Admin
from Applicant import Applicant
from CourseSection import CourseSection
from Faculty import Faculty
from FacultySection import FacultySection
from Staff import Staff
from Student import Student
from StudentSection import StudentSection
from Section import Section
from User import User

db = SqliteDatabase('studentdatabase.db')

db.connect()
db.create_tables([User, Student, Staff, Admin, Faculty, Applicant, Course, Section, CourseSection, FacultySection, StudentSection], safe = True)
