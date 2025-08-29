# Find and display the largest number of a list without using built-in function max(). Your program should
 #ask the user to input values in list from keyboard.


input_string = input("Enter numbers using spaces:")

num_string = [int(num) for num in input_string.split()]

largest_num = num_string[0]

for num in num_string:
    if num > largest_num:
        largest_num = num

print("Largest number is:", largest_num)

