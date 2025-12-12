students=[]
courses=[]

class student():
    def __init__(self,id_Student,name_Student,DoB):
        self.id_Student=id_Student
        self.name_Student=name_Student
        self.DoB=DoB
        self.smark={}
class course():
    def __init__(self,id_course,name_course):
        self.id_course=id_course
        self.name_course=name_course

class mark():
    def __init__(self,smark):
        self.smark=smark

def check_course(select_course):
    find_c=None
    for i in courses:
        if i.id_course==select_course or i.name_course==select_course:
            find_c=i
    if (find_c==None):
        print("No info course") 
        return
    print(f'Select courses {find_c.name_course}')
    select_student=input('Input name or id student :')
    find_s=None
    for i in students:
        if i.id_Student==select_student or i.name_Student==select_student:
            find_s=i
    if (find_s==None): 
        print("No info student")
        return
    find_s.mark[find_s]=input("Input mark")

def list_students():
    for i in students:
        print(f"ID: {i.id_Student}, Name:{i.name_Student}, DoB:{i.DoB}")

def list_courses():
    for i in courses:
        print(f"ID: {i.id_course}, Name: {i.name_course}")

numberc=input("Input number of courses :")
for i in range (int(numberc)):
    idc=input(f"Input id course {i+1} :")
    namec=input("Input name course :")
    new_c=course(idc,namec)
    courses.append(new_c)
    numbers=input("Input the number of students in a class :")
    for i in range (int(numbers)):
        id=input(f"Input id student {i+1} :")
        name=input("Input name :")
        DoB=input("Input DoB :")
        new_s=student(id,name,DoB)
        students.append(new_s)
select_course=input("Input id or name course to choose course:")
check_course(select_course)
print("Info students :")
list_students()
print("Info courses :")
list_courses()

