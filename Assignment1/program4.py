#take four digit number and display face value,
# place value and display in reverse order 

def four_digit_number(num):
    
    if not (1000 <= num <= 9999):
        print(" enter a valid 4-digit number.")
        return

    print("1. Face values:")
    for digit_char in str(num):
        print(digit_char, end="  ")
    print("\n")

    print("2. Place values:")
    thousands = (num // 1000) * 1000
    hundreds = ((num % 1000) // 100) * 100
    tens = ((num % 100) // 10) * 10
    ones = num % 10
    print(f"{num} = {thousands} + {hundreds} + {tens} + {ones}\n")

    
    print("3. Number in reverse order:")
    reverse_number = int(str(num)[::-1])
    print(reverse_number)


user_input = int(input("Enter a 4-digit number: "))
four_digit_number(user_input)