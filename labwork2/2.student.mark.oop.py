

import time
import numpy as np
import math

class Course:  # TODO: add student and the mark , add credit
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
    def __init__(self, number_student: int, student: list) -> None:
        super().__init__(id, name)
        self._number_student = None
        self._student = None
        self.setNumberStudent(number_student)
        self._student = student

    def setNumberStudent(self, number_student: int) -> None:
        self.validateNumberStudent(number_student)
        self._number_student = number_student

    def getNumberStudent(self) -> int:
        return self._number_student

    def validateNumberStudent(self, number_student: int) -> None:
        if not isinstance(number_student, int):
            raise TypeError("Number of students should be an integer.")
        elif number_student < 0:
            raise ValueError("Number of students should be greater than or equal to 0.")



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
    def __init__(self, name: str, student_id: int, DoB: str, course=[], GPA =0):
        super().__init__(name, DoB)
        self.validateStudentId(student_id)
        # self.validateCourse(course)

        self._student_id = student_id
        self._course = course
        self._GPA = GPA

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

    def addCourse(self, course):  # TODO:
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


def student_info():  # done
    student_id = int(input("Enter student's id: "))
    name = input("Enter student name: ")
    date_of_birth = input("Enter student's DoB: ")
    stu = Student(name, student_id, date_of_birth, [])
    return stu


def student_list():  # done
    print("\nWe have the list of students: ")
    for student in class_student["students"]:
        print("ID: " + str(student["_student_id"]) + "\nName: " + student["_name"] + "\nDoB: " + student[
            "_DoB"] + "\nCourse: " + str(student["_course"]) + "\n")


def class_number_students():  # done
    student_number = int(input("How many student?\n- "))
    class_student["number"] = student_number
    for i in range(student_number):
        class_student["students"].append(student_info().getStudent())


def list_course():  # this is to add my courses
    course_number = int(input("Enter number of course: "))
    course["number"] = course_number
    for i in range(course_number):
        course_name = input("Enter course name: ")
        course_id = int(input("Enter course id: "))
        course_credit = int(input("Enter course credit: "))
        x = Course(course_name, course_id, course_credit, [])
        course["courses"].append(x.addCourse())
    for cour in course["courses"]:
        print(cour)

def course_list():  # done
    for cour in course["courses"]:
        print("ID: " + str(cour["_course_id"]) + " --- Name: " + cour["_course_name"])
        print("Credit: " + str(cour["_course_credit"]))
        print(cour["_course_mark"])


def course_mark():
    print("\nWe have courses: ")
    course_list()
    course_id = int(input("\nPlease enter course's id to enter mark: "))
    student_name = input("Please enter student's name: ")
    mark = math.floor(int(input("Please enter student's mark: ")))
    course_name = ""
    cre = 0
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            course_name = cour["_course_name"]
            cre = cour["_course_credit"]
            cour["_course_mark"].append([student_name, mark])
            break
    for student in class_student["students"]:
        if student["_name"] == student_name:
            for course_taken in student["_course"]:
                if course_taken[0] == course_name:
                    course_taken[1] = mark
                    course_taken[2] = cre
                    break
    print(f"Mark of {student_name} in {course_name} has been updated to {mark}")



def show_mark():  # TODO
    course_id = int(input("Please enter course id to see the marks: "))
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            for i in range(2, len(cour)):
                print(cour["_course_mark"])

def calculateGPA():
    total_mark = 0
    total_credit = 0
    for student in class_student["students"]:
        for cour in student["_course"]:
            total_mark += cour[1]*cour[2]
            total_credit += cour[2]
        gpa = total_mark/total_credit
        student["_GPA"] = gpa

def array():
    arr = []
    for student in class_student["students"]:
        arr += [[student["_name"], student["_GPA"]]]
    return arr

def rank():
    students_gpa = array()
    sorted_gpa = sorted(students_gpa, key=lambda x: x[1], reverse=True)
    print("Ranking of Students based on GPA:")
    for index, student in enumerate(sorted_gpa):
        print(f"{index+1}. {student[0]}: {student[1]}")


def menu():
    print("""
    Please choose your action:
    Add Student: 1
    Show Students: 2
    Add Courses: 3
    Show Course: 4
    Add Mark: 5
    Show Mark: 6
    Calculate GPA: 7
    Exit: 8
    """)

def engine():
    menu()
    act = int(input("Enter number of action: "))
    if act == 1:
        class_number_students()
        time.sleep(2)
        engine()
    elif act == 2:
        student_list()
        time.sleep(2)
        engine()
    elif act == 3:
        list_course()
        time.sleep(2)
        engine()
    elif act == 4:
        course_list()
        time.sleep(2)
        engine()
    elif act == 5:
        course_mark()
        time.sleep(2)
        engine()
    elif act == 6:
        show_mark()
        time.sleep(2)
        engine()
    elif act == 7:
        calculateGPA()
        time.sleep(2)
        engine()
    elif act == 8:
        print("Bye bye")
        return None
    else:
        raise Exception("You did not enter the given menu")

if __name__ == '__main__':
    #class_number_students()
    #list_course()

    engine()
    student_list()
    for student in class_student["students"]:
        print(student)




    


