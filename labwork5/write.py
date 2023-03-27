courses = "C:\Git\pp2023\labwork5\information\courses.txt"
marks = "C:\Git\pp2023\labwork5\information\marks.txt"
students = "C:\Git\pp2023\labwork5\information\students.txt"

# class_student = {
#     "number": 0,
#     "students": [{'_name': 'hieu', '_DoB': '15', '_student_id': 1, '_course': [['dip', 15, 4], ['oop', 16, 5]], '_GPA': 15},
#                  {'_name': 'ngoc', '_DoB': '20', '_student_id': 2, '_course': [['dip', 11, 4], ['oop', 12, 5]], '_GPA': 13}]
# }
# course = {
#     "number": 0,
#     "courses": [{'_course_name': 'dip', '_course_id': 1, '_course_credit': 4, '_course_mark': [['hieu', 15], ['ngoc', 11]]},
#                 {'_course_name': 'oop', '_course_id': 2, '_course_credit': 5, '_course_mark': [['hieu', 15], ['ngoc', 16]]}]
# }



def get_text_students_file(students, class_student):
    f = open(students, "w")
    for student in class_student["students"]:
        f.write("\nID: " + str(student["_student_id"]) + "\nName: " + student["_name"] + "\nDoB: " + student[
            "_DoB"] + "\nCourse: " + str(student["_course"]) + "\n")
    f.close()

def get_text_courses_file(courses, course):
    f = open(courses, "w")
    for cour in course["courses"]:
        f.write("\nID: " + str(cour["_course_id"]) + " --- Name: " + cour["_course_name"] + "\nCredit: " + str(cour["_course_credit"]) + "\n" + str(cour["_course_mark"]) + "\n")
    f.close()

def get_text_marks_file(marks, class_student):
    f = open(marks, "w")
    for student in class_student["students"]:
        f.write("\nID: " + str(student["_student_id"]) + "\nName: " + student["_name"] + "\nCourse: " + str(student["_course"]) + "\nGPA: " + str(student["_GPA"]) + "\n")
    f.close()