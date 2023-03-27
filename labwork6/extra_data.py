import string

def Convert(string):
    li = list(string.split(" "))
    return li

if __name__ == '__main__':
    mylines = []
    with open ('info/marks.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline.rstrip('\n'))
    print(mylines)
    i = 1
    mul = 0
    ID = []
    Name = []
    Course = []
    GPA = []
    max_mul = len(mylines)/5
    for line in mylines:
        if i == 2 + mul*5:
            ID.append(line[4:])
        elif i == 3 + mul*5:
            Name.append(line[6:])
        elif i == 4 + mul*5:
            Course.append(line[8:])
        elif i == 5 + mul*5:
            GPA.append(line[5:])
        if i%5==0:
            mul = mul + 1
        i = i+1



    x=[]
    for c in range(0,len(Course)):
        list = []

        print(Course[c].split("]"))
        a = 0
        for i in Course[c].split("]"):
            if a == 0 and len(i) > 1:
                list.append(i[2:])
            elif len(i) > 1:
                list.append(i[3:])
            a = a + 1
        for i in range(len(list)):
            print(list[i].split(", "))
            x = x + list[i].split(", ")
        for i in range(0,len(x),3):
            x[i] = x[i].rstrip(string.punctuation).lstrip(string.punctuation)
            x[i+1] = int(x[i+1])
            x[i+2] = int(x[i+2])
    print(x)