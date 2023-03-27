import pickle

class_student = {
    "number": 0,
    "students": [{'_name': 'eny', '_DoB': '15', '_student_id': 1, '_course': [['dip', 15, 4], ['oop', 16, 5]], '_GPA': 15},
                 {'_name': 'thao', '_DoB': '20', '_student_id': 2, '_course': [['dip', 11, 4], ['oop', 12, 5]], '_GPA': 13}]
}

def dip(class_student):
    pickle_out = open("student.pickle", "wb")
    pickle.dump(class_student, pickle_out)
    pickle_out.close()

def use():
    pickle_in = open("student.pickle", "rb")
    class_student = pickle.load(pickle_in)
    return class_student

if __name__ == '__main__':
    print(use())
