import numpy as np
import math
import curses
from domains.student import Student
from domains.course import Course
from output import course_list

def student_info(screen):  # done
    screen.addstr("Enter student's id: ")
    student_id = int(screen.getstr().decode())
    screen.addstr("Enter student's name: ")
    name = screen.getstr().decode()
    screen.addstr("Enter student's DoB: ")
    date_of_birth = screen.getstr().decode()
    stu = Student(name, student_id, date_of_birth, [], 0)
    return stu

def class_number_students(screen, class_student):  # TODO
    screen.addstr("How many student?\n- ")
    student_number = int(screen.getstr().decode())
    class_student["number"] = student_number
    for i in range(student_number):
        class_student["students"].append(student_info(screen).getStudent())

def list_course(screen , course):  # TODO
    screen.addstr("Enter number of course:\n - ")
    course_number = int(screen.getstr().decode())
    course["number"] = course_number
    for i in range(course_number):
        screen.addstr("Enter course name:\n - ")
        course_name = screen.getstr().decode()
        screen.addstr("Enter course id:\n - ")
        course_id = int(screen.getstr().decode())
        screen.addstr("Enter course credit:\n - ")
        course_credit = int(screen.getstr().decode())
        x = Course(course_name, course_id, course_credit, [])
        course["courses"].append(x.addCourse())
        
def course_mark(screen, course, class_student):  # TODO
    screen.addstr("\nWe have courses: \n")
    course_list(screen, course)
    screen.addstr("\nPlease enter course's id to enter mark: ")
    course_id = int(screen.getstr().decode())
    screen.addstr("Please enter student's name: ")
    student_name = screen.getstr().decode()
    screen.addstr("Please enter student's mark: ")
    mark = math.floor(int(screen.getstr().decode()))
    course_name = ""
    cre = 0
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            course_name = cour["_course_name"]
            cre = cour["_course_credit"]
            cour["_course_mark"].append([student_name, mark])
        else:
            cour["_course_mark"] = cour["_course_mark"]
    for student in class_student["students"]:
        if student["_name"] == student_name:
            student["_course"].append([course_name, mark, cre])