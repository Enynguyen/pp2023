import numpy as np
import math
import curses
import compress
from input import *
from output import *
from write import *



class_student = {
    "number": 0,
    "students": []
}

course = {
    "number": 0,
    "courses": []
}

def menu(screen):
    screen.addstr("Please choose your action:\nAdd Student: 1\nShow Students: 2\nAdd Courses: 3\nShow Course: 4\nAdd Mark: 5\nShow Mark: 6\nCalculate GPA: 7\nSorted GPA: 8\nExit: 9")
    screen.addstr("\n\nEnter your action: ")
    screen.refresh()
    curses.napms(2000)

def clear(screen):
    screen.refresh()
    curses.napms(2000)
    screen.clear()
    screen.refresh()
    curses.endwin()

def engine(screen):

    menu(screen)
    act = int(screen.getstr().decode())
    if act == 1:
        class_number_students(screen, class_student)
        clear(screen)
        engine(screen)
    elif act == 2:
        student_list(screen, class_student)
        clear(screen)
        engine(screen)
    elif act == 3:
        list_course(screen, course)
        clear(screen)
        engine(screen)
    elif act == 4:
        course_list(screen, course)
        clear(screen)
        engine(screen)
    elif act == 5:
        course_mark(screen, course, class_student)
        clear(screen)
        engine(screen)
    elif act == 6:
        show_mark(screen, course)
        clear(screen)
        engine(screen)
    elif act == 7:
        calculateGPA(screen, class_student)
        clear(screen)
        engine(screen)
    elif act == 8:
        rank(screen, class_student)
        clear(screen)
        engine(screen)
    elif act == 9:
        screen.addstr("Bye bye")
        get_text_students_file(students, class_student)
        get_text_courses_file(courses, course)
        get_text_marks_file(marks, class_student)
        clear(screen)
    else:
        raise Exception("You did not enter the given menu")


if __name__ == '__main__':
    compress.extract_data(class_student, course)
    # for a in class_student["students"]:
    #     print(a)
    screen = curses.initscr()
    engine(screen)