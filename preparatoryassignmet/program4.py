#. Write a program to calculate the grade of a student. There are five 
#subjects. Marks in each subject are entered from keyboard. Assign grade 
#based on the following rule: 
#Total Marks >= 90   Grade: Ex 
#90 > Total Marks >= 80  Grade: A 
#80 > Total Marks >= 70  Grade: B 
#70 > Total Marks >= 60  Grade: C 
#60 > Total Marks    Grade: F
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
average = total_marks / 5

if average >= 90:
    grade = "Ex"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

print(f"\nTotal Marks: {total_marks:.2f}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")