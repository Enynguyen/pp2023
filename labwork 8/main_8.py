import numpy as np
import math
import compress
from input import *
from output import *
from write import *
import pickle, compress, curses, threading


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

def dip_1(course):
    pickle_out = open("course.pickle", "wb")
    pickle.dump(course, pickle_out)
    pickle_out.close()

def dip_2(class_student):
    pickle_out = open("student.pickle", "wb")
    pickle.dump(class_student, pickle_out)
    pickle_out.close()

def use1():
    pickle_in = open("student.pickle", "rb")
    class_student_1 = pickle.load(pickle_in)
    pickle_in.close()
    return class_student_1

def use2():
    pickle_in = open("course.pickle", "rb")
    course_1 = pickle.load(pickle_in)
    pickle_in.close()
    return course_1

if __name__ == '__main__':
    compress.file_listing()
    for file in compress.file_listing():
        if file == "student.pickle":
            class_student = use1()
            course = use2()
    # compress.extract_data(class_student, course)
    # for a in class_student["students"]:
    #     print(a)
    screen = curses.initscr()
    engine(screen)
    end1 = threading.Thread(target=dip_1(course))
    end2 = threading.Thread(target=dip_2(class_student))
    end1.start()
    end2.start()
    end1.join()
    end2.join()