import time
import numpy as np
import math
import curses

class Course:  # done
    def __init__(self, course_name: str, course_id: int, course_credit = 0, mark=[]):
        self.validateCourse_name(course_name)
        self.validateCourse_id(course_id)

        self._course_name = course_name
        self._course_id = course_id
        self._course_mark = mark #should'n make default parameter make it like this _course_mark = mark
        self._course_credit = course_credit

    def setCourse_name(self, course_name):
        self.validateCourse_name(course_name)
        self._course_name = course_name

    def getCourse_name(self):
        return self._course_name

    def validateCourse_name(self, course_name: str):
        if not isinstance(course_name, str):
            raise TypeError("Type is not valid")
        elif len(course_name) < 1:
            raise Exception("Sorry length of the cousre's name must be longer than 1")

    def setCourse_id(self, course_id):
        self.validateCourse_id(course_id)
        self._course_id = course_id

    def getCourse_id(self):
        return self._course_id

    def validateCourse_id(self, course_id):
        if not isinstance(course_id, int):
            raise TypeError("Type is not valid")
        elif course_id < 0:
            raise Exception("Sorry course id cannot be negative")

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def addCourse(self):
        return self.__dict__


class MyClass(Course):

    def __init__(self, number_student: int, student: list):  # auto update the value and the list in stu

        self.validateNumberStudent(number_student)

        self.age = number_student

    def setNumberStudent(self, number_student):
        self.validateNumberStudent(number_student)
        self.number_student = number_student

    def getNumberStudent(self):
        return self.number_student

    def validateNumberStudent(self, number_student: int):
        if not isinstance(number_student, int):
            raise TypeError("Type is not valid")
        elif number_student < 0:
            raise Exception("Sorry number of student is not valid")


class Person:
    def __init__(self, name, DoB):
        self.validateName(name)
        self.validateDoB(DoB)

        self._name = name
        self._DoB = DoB

    def setName(self, name):
        self.validateName(name)
        self._name = name

    def getName(self):
        return self._name

    def validateName(self, name):
        if not isinstance(name, str):
            raise TypeError("Type of is not valid")
        elif len(name) < 0 or len(name) > 100:
            raise Exception("Name is not valid")

    def setDoB(self, DoB):
        self.validateDoB(DoB)
        self._DoB = DoB

    def getDoB(self):
        return self._DoB

    def validateDoB(self, DoB):
        if not isinstance(DoB, str):
            raise TypeError("Type is not valid")
        elif len(DoB) < 0:
            raise Exception("DoB id is not valid")


class Student(Person):
    def __init__(self, name: str, student_id: int, DoB: str, course=[], mark = 0):
        super().__init__(name, DoB)
        self.validateStudentId(student_id)
        # self.validateCourse(course)

        self._student_id = student_id
        self._course = course
        self._GPA = mark

    def setName(self, name):
        super().validateName(name)

    def getName(self):
        super().getName()

    def validateName(self, name: str):
        super().validateName(name)

    def setStudent_id(self, student_id):
        self.validateStudent_id(student_id)
        self._student_id = student_id

    def getStudent_id(self):
        return self._student_id

    def validateStudentId(self, student_id: int):
        if not isinstance(student_id, int):
            raise TypeError("Type is not valid")
        elif student_id < 0:
            raise Exception("Student id is not valid")

    def setDoB(self, DoB):
        super().setDoB(DoB)

    def getDoB(self):
        super().getDoB()

    def validateDoB(self, DoB: str):
        super().validateDoB(DoB)

    def addCourse(self, course):  # done
        self._course.append(course)

    def getCourse(self):
        return self._course

    def validateCourse(self, course: list):
        if not isinstance(course, list):
            raise TypeError("Type is not valid")
        elif course < 0:
            raise Exception("Course id is not valid")

    def getStudent(self):
        return self.__dict__


class_student = {
    "number": 0,
    "students": []
}

course = {
    "number": 0,
    "courses": []
}


def student_info(screen):  # done
    screen.addstr("Enter student's id: ")
    student_id = int(screen.getstr().decode())
    screen.addstr("Enter student's name: ")
    name = screen.getstr().decode()
    screen.addstr("Enter student's DoB: ")
    date_of_birth = screen.getstr().decode()
    stu = Student(name, student_id, date_of_birth, [], 0)
    return stu


def student_list(screen):  # done
    screen.addstr("\nWe have the list of students: ")
    for student in class_student["students"]:
        screen.addstr("ID: " + str(student["_student_id"]) + "\nName: " + student["_name"] + "\nDoB: " + student[
            "_DoB"] + "\nCourse: " + str(student["_course"]) +"\nGPA: "+ str(student["_GPA"]) + "\n")


def class_number_students(screen):  # done
    screen.addstr("How many student?\n- ")
    student_number = int(screen.getstr().decode())
    class_student["number"] = student_number
    for i in range(student_number):
        class_student["students"].append(student_info(screen).getStudent())


def list_course(screen):  # this is to add my courses
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
        
        
def course_list(screen):  # done
    for cour in course["courses"]:
        screen.addstr("ID: " + str(cour["_course_id"]) + " --- Name: " + cour["_course_name"] + "\n")
        screen.addstr("Credit: " + str(cour["_course_credit"])+"\n")
        for mark in cour["_course_mark"]:
            screen.addstr(str(mark)+"\n")


def course_mark(screen):  # done
    screen.addstr("\nWe have courses: ")
    course_list(screen)
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


def show_mark(screen):  # done
    screen.addstr("Please enter course id to see the marks:\n- ")
    course_id = int(screen.getstr().decode())
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            for i in range(2, len(cour)):
                screen.addstr(cour["_course_mark"])

def calculateGPA(screen):
    total_mark = 0
    total_credit = 0
    for student in class_student["students"]:
        gpa = 0
        for cour in student["_course"]:
            total_mark += cour[1]*cour[2]
            total_credit += cour[2]
            gpa = total_mark/total_credit
        student["_GPA"] = gpa
    student_list(screen)

def array():
    arr = []
    for student in class_student["students"]:
        arr += [[student["_name"], student["_GPA"]]]
    return arr

def list_gpa(): #done
    gpas = np.array([])
    for student in class_student["students"]:
        gpas = np.concatenate((gpas, [int(student["_GPA"])]))
    return gpas

def rank(screen):
    x = []
    sorted = np.sort(list_gpa())[::-1]
    for student in class_student["students"]:
        x.append([student["_name"], int(student["_GPA"])])
    screen.addstr("We have the list of sorted student in descending order:\n")
    for gpa in sorted:
        for stu in x:
            if gpa == stu[1]:
                screen.addstr(stu[0] + "\n")
                x.remove(stu)

def menu(screen):
    screen.addstr(
        "Please choose your action:\nAdd Student: 1\nShow Students: 2\nAdd Courses: 3\nShow Course: 4\nAdd Mark: 5\nShow Mark: 6\nCalculate GPA: 7\nSorted GPA: 8\nExit: 9")
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
        class_number_students(screen)
        clear(screen)
        engine(screen)
    elif act == 2:
        student_list(screen)
        clear(screen)
        engine(screen)
    elif act == 3:
        list_course(screen)
        clear(screen)
        engine(screen)
    elif act == 4:
        course_list(screen)
        clear(screen)
        engine(screen)
    elif act == 5:
        course_mark(screen)
        clear(screen)
        engine(screen)
    elif act == 6:
        show_mark(screen)
        clear(screen)
        engine(screen)
    elif act == 7:
        calculateGPA(screen)
        clear(screen)
        engine(screen)
    elif act == 8:
        rank(screen)
        clear(screen)
        engine(screen)
    elif act == 9:
        screen.addstr("Bye bye")
        clear(screen)
    else:
        raise Exception("You did not enter the given menu")


if __name__ == '__main__':
    screen = curses.initscr()
    engine(screen)






