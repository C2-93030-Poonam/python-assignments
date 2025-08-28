# Write a program to read the name of a student (studentName), roll 
#Number (rollNo) and marks (totalMarks) obtained. rollNo may be an 
#alphanumeric string. Display the data as read. Hint: Create a Student 
#structure and write appropriate functions. 


class Student:
    def __init__(self, studentName, rollNo, totalMarks):
        self.studentName = studentName
        self.rollNo = rollNo
        self.totalMarks = totalMarks

    def display(self):
        print("\n--- Student Details ---")
        print(f"Name       : {self.studentName}")
        print(f"Roll No    : {self.rollNo}")
        print(f"Total Marks: {self.totalMarks}")


def read_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number (alphanumeric): ")
    marks = float(input("Enter total marks obtained: "))
    return Student(name, roll, marks)


student = read_student()
student.display()