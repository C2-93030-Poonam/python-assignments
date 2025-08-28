#find maximum no.s from three nos

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
elif num3 >= num1 and num3 >= num2:
    max_num = num3
print("maximum number is:" ,max_num)    

