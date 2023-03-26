import numpy as np
import math
import curses

def student_list(screen, class_student):  # TODO
    screen.addstr("\nWe have the list of students: ")
    for student in class_student["students"]:
        screen.addstr("ID: " + str(student["_student_id"]) + "\nName: " + student["_name"] + "\nDoB: " + student[
            "_DoB"] + "\nCourse: " + str(student["_course"]) +"\nGPA: "+ str(student["_GPA"]) + "\n")

def course_list(screen, course):  # TODO
    for cour in course["courses"]:
        screen.addstr("ID: " + str(cour["_course_id"]) + " --- Name: " + cour["_course_name"] + "\n")
        screen.addstr("Credit: " + str(cour["_course_credit"])+"\n")
        for mark in cour["_course_mark"]:
            screen.addstr(str(mark)+"\n")

def show_mark(screen, course):  # TODO
    screen.addstr("Please enter course id to see the marks:\n- ")
    course_id = int(screen.getstr().decode())
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            for i in range(2, len(cour)):
                screen.addstr(cour["_course_mark"])

def calculateGPA(screen, class_student): # TODO
    total_mark = 0
    total_credit = 0
    for student in class_student["students"]:
        gpa = 0
        for cour in student["_course"]:
            total_mark += cour[1]*cour[2]
            total_credit += cour[2]
            gpa = total_mark/total_credit
        student["_GPA"] = gpa
    student_list(screen, class_student)

def array(class_student):# TODO
    arr = []
    for student in class_student["students"]:
        arr += [[student["_name"], student["_GPA"]]]
    return arr

def list_gpa(class_student):# TODO
    gpas = np.array([])
    for student in class_student["students"]:
        gpas = np.concatenate((gpas, [int(student["_GPA"])]))
    return gpas

def rank(screen, class_student): # TODO
    x = []
    sorted = np.sort(list_gpa(class_student))[::-1]
    for student in class_student["students"]:
        x.append([student["_name"], int(student["_GPA"])])
    screen.addstr("We have the list of sorted student in descending order:\n")
    for gpa in sorted:
        for stu in x:
            if gpa == stu[1]:
                screen.addstr(stu[0] + "\n")
                x.remove(stu)