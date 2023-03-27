import zipfile
import os
import init

def file_listing():
    basepath = 'C:\Git\pp2023\labwork 5'
    flist = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            flist.append(entry)
    return flist

def extract_data(class_student, course):
    file_listing()
    for file in file_listing():
        if file == "students.dat":
            data_zip = zipfile.ZipFile('students.dat', 'r')
            data_zip.extractall(path='.')
            init.Init(class_student, course)

def compress():
    try:
        file_list = ["info/courses.txt"
            , "info/marks.txt"
            , "info/students.txt"]
        with zipfile.ZipFile('students.dat', 'w') as new_zip:
            for name in file_list:
                new_zip.write(name)
    except FileNotFoundError as e:
        print(f' *** Exception occurred during zip process - {e}')