#. Write a program to input n numbers on command line argument and 
#calculate maximum of them. 

import sys

if len(sys.argv) < 2:
    print("Please provide numbers as command line arguments.")
    sys.exit()

numbers = [float(arg) for arg in sys.argv[1:]]

max_value = max(numbers)

print(f"Maximum value is: {max_value}")