from .person import Person
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