# Function
# def function_name(arguments):
#     """"docstring"""
# statement1
# statement2

# Call 
# Function_name("a value")

# example
# def greet(name):
#     print("Hello, " + name + ". Good morning!")

# greet("Emma")

# len(arg): number of elenments in arg
# print(args): write args to stdout
# input(promp): print(prompt), ưait and read user input from stdin, return
# the enters string

# SET
# operator
#    + s1.isdisjoint(s2) : no common element02

#    + s1 <= s2, s1.issubset(s2)...

# slicing similar to strings
#    * seq[start:end:step]

# >> names = ["ICT", "ict"]
# + name += ["Ict"]
# ==> names ["ICT", "ict", "Ict"]
# + replacing single Value : names[1] = " i see Tea"

# >>> names ["ICT", " i see Tea", "Ict"]
# + replaces bunch of values
#  >>> names [1:3] = ["Icy Tea", "I see tea"]
#  >>> names["ICT", "Icy Tea", "I see tea"]

# + += append elenment at middle, sane as .insert()
# >>> names[1:1] += ["Icy City"]
# >>> names['ICT', 'Ice City', 'Icy Tea', 'I See Tea']

# + sort() elements

# >>> names
# ['ICT', 'Ice City', 'Icy Tea', 'I See Tea']

# >>> names.sort()
# >>> names['I See Tea', 'ICT', 'Ice City', 'Icy Tea']

# >>> del names[1]
# >>>names
# ['I See Tea', 'Ice City', 'Icy Tea']

# >>>names.remove("Icy Tea")
# >>> names
# ['Ice City', 'I See Tea']

# -- Map operations

# * Value operations
# d[k]: get value by Key
# d[k] = v: set value to Key
# del d[k] : remove key from dict

# --Maps: methods
# * d.get(k[, default]) : same as d[k], fallback to default if key not found
# * d.keys() : returns list of keys
# * d.values() : return listh of values
# * d.items() : return list of (key, value) tuples.


# Practical work 1


Students = []
courses = []

# Input the number of students in a class
def class_students():
    num_Stu = int(input("Enter the total students: "))
    
    return num_Stu

# Input student information: ID, name, DoB
def student_info():
    student_id = int(input("ID_student: "))
    student_name = input("Name_student: ")
    DoB = input("Your birthday: ")
    Student = {"ID": student_id, "Name": student_name, "DoB":  DoB, "courses": []}
    Students.append(Student)
    return Students
    
# Input number of courses
def class_courses():
    num_course = int(input("Input the number of courses: "))
    return num_course

# Input course information: id, name
def course_info():
    course_ID = int(input("course_ID: "))
    course_name = input("course_name: ")
    course = {"id": course_ID, "name": course_name}
    courses.append(course)

# List students
def students_list():
    print("\nWe have list_Students: ")
    for student in Students:
        print('ID: {student["ID"]} \nName: {student["Name"]} \nDoB: {student["DoB"]} \nCourse: {student["courses"]}\n')

# List courses
def course_list():
    print("Lis_coures: " )
    for course in courses:
        print(course["id"], course["name"])

# select a course, input marks for student in this course
def course_mark():
    print("Total_courses:  ")
    course_list()
    course_id = int(input("\nPlease enter course's id to enter mark: "))
    student_name = input("Please enter student's name: ")
    mark = int(input("Enter student_mark: "))
    course_name = ""
    for course in courses:
        if course["id"] == course_id:
            course_name = course["name"]
            course["marks"] = {student_name: mark}
    for student in Students:
        if student["Name"] == student_name:
            student["courses"].append(course_name)

def show_mark():
    course_id = int(input("Please enter course id to see the marks: "))
    for course in courses:
        if course["id"] == course_id:
            print("Marks for course", course["name"])
            for student, mark in course["marks"].items():
                print(student, mark)

class_students()
students_list()
num_courses = class_courses()
for i in range(num_courses):
    course_info()
course_list()
course_mark()
show_mark()
