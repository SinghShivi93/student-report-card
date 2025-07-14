#Student Report Card Generator
#Student ka naam aur class liya jaayega
#Subjects and marks user input karega
#Total marks calculate honge
#Average nikalega
#Grade assign karegi (like A, B, C)
print("Welcome to Report Card Generator 📝")
name = (input("Enter student name: "))
Class = (input("Enter class: "))
sub_count = (int(input("How many subjects? ")))
SubjectList = []
MarksList = []
TotalMarks = 0
for i in range(sub_count):
    sub_name = input(f"Enter subject {i+1} name: ")
    SubjectList.append(sub_name)
    sub_marks = float(input("Enter marks: "))
    MarksList.append(sub_marks)
    TotalMarks = TotalMarks + MarksList[i]

AverageMarks = TotalMarks / len(SubjectList)

print(f"📋 Report Card for {name} - Class {Class}")
for i in range(len(SubjectList)):
    print(f"{i+1}: {SubjectList[i]} - {MarksList[i]}")
print(f"Your Total Marks: {TotalMarks}")
print(f"Your Average Marks: {AverageMarks}")

if AverageMarks >= 90:
    print('grade = A+')
elif AverageMarks >= 75:
    print('grade = A')
elif AverageMarks >= 60:
    print('grade = B')
elif AverageMarks >= 40:
    print('grade = C')
else:
    print('grade = Fail')
print("Thankyou")
