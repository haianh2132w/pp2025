students=[]
courses=[]

def student(name_c,id_c):
    number_student=input("Number of students in a class:")
    for i in range(int(number_student)):
        name=input(f"Name s{i+1}:")
        id=input("ID :")
        dob=input("dob :")
        students.append({"Name": name,"ID":id,"dob":dob,"mark":{},"name course":name_c,"id course":id_c})

def course(number_course):
    for i in range (int (number_course)):
        name=input("Name course:")
        id=input("ID :")
        courses.append({"Name": name,"ID":id})
        student(name,id)

def mark(course):
    print("Input mark for student in "+course)
    for student in students:
        if(student["name course"]==course):
            s_mark=float(input(f"Student {student['Name']} (ID:{student['ID']}): "))
            student["mark"][course]=s_mark

def check_course(choose_course):
    for i in courses:
        if i["Name"]==choose_course or i["ID"]==choose_course:
            mark(i["Name"])
            return
    print("No infomation")
    
def display():
    print("List students :")
    for i in students:
        print(i)
    print("List courses: ")
    for i in courses:
        print(i)
    print("List marks :")
    for i in students:
        print(i["Name"],i["mark"])


number_course=input("Number of courses :")
course(number_course)

choose_course=input("Input id or name to choose course :")
check_course(choose_course)

display()