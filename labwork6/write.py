courses = "C:\Git\pp2023\labwork6\information\courses.txt"
marks = "C:\Git\pp2023\labwork6\information\marks.txt"
students = "C:\Git\pp2023\labwork6\information\students.txt"



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




