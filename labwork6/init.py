from domains.student import Student
from domains.course import Course
import math
import string
from main_2 import *

# from labwork6 import main_2



def Init(class_student, course):
    mylines = []
    with open('info/marks.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline.rstrip('\n'))
    i = 1
    mul = 0
    ID = []
    Name = []
    courses = []
    GPA = []
    for line in mylines:
        if i == 2 + mul * 5:
            ID.append(line[4:])
        elif i == 3 + mul * 5:
            Name.append(line[6:])
        elif i == 4 + mul * 5:
            courses.append(line[8:])
        elif i == 5 + mul * 5:
            GPA.append(line[5:])
        if i % 5 == 0:
            mul = mul + 1
        i = i + 1
    DoB = []
    with open('info/students.txt', 'rt') as myfile:
        for line in myfile:
            if line.find("DoB") == 0:
                DoB.append(line.rstrip('\n'))
    for i in range(len(ID)):
        stu = Student(Name[i], int(ID[i]), DoB[i][5:], [], float(GPA[i]))
        class_student["students"].append(stu.getStudent())

    #TODO
    #extract function
    t = []
    for c in range(0, len(courses)):
        list = []
        a = 0
        for i in courses[c].split("]"):
            if a == 0 and len(i) > 1:
                list.append(i[2:])
            elif len(i) > 1:
                list.append(i[3:])
            a = a + 1
        for i in range(len(list)):
            t = t + list[i].split(", ")
        for i in range(0, len(t), 3):
            t[i] = t[i].rstrip(string.punctuation).lstrip(string.punctuation)
            t[i + 1] = int(t[i + 1])
            t[i + 2] = int(t[i + 2])
    count = len(t)/6 #TODO
    #after i got x start to fill in wait needed
    #Remember that thi student course now is still not in a correct form
    id = 1
    for i in range(0,len(t),3):
        x = Course(str(t[i]), int(id), int(t[i+2]), [])
        id = id + 1
        course["courses"].append(x.addCourse()) #TODO
        count = count - 1
        if count == 0: break
    #Add mark time
    ind = 0
    for student in class_student["students"]:
        for num in range(0,2):
            student["_course"].append([t[ind], t[ind+1], t[ind+2]])
            ind = ind + 3

    #TODO: add marks to course
    cor = 0
    for i in range(len(class_student["students"])):
        for m in range(len(course["courses"])): #TODO
            course["courses"][m]["_course_mark"].append([class_student["students"][i]["_name"], class_student["students"][i]["_course"][m][1]])
    