#  Write A Program which is taking 5 int value and calculate 
# sum of cube of all numbers [Write cube function]


def cube(n):
    return n ** 3

numbers = []

print("Enter 5 integer values:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

sum_of_cubes = sum(cube(n) for n in numbers)

print("Sum of cubes of the given numbers is:", sum_of_cubes)