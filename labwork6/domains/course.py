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