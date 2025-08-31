#. Write a function in python to count the number of #lines from a text file "story.txt" which is not starting
# with an alphabet "C".
# Example: If the file "test.txt" contains the following #lines:
 #Connecting DB’s with Python.
 #Working with DB’s using Python.
 #Accessing and Manipulating DB’s.
 #Creation of Python virtual Environment.
 #Working with beautiful soup.
 #Working with matplotlib, seaborn.
 #The function should display the output as 4

def count_non_c_lines(filename):
    count = 0
    with open("d:\\pythonassignments\\python-module\\python-assignments\\Assignment7\\story.txt", 'r') as file:
        for line in file:
            stripped_line = line.lstrip()  # Remove leading whitespace
            if not stripped_line.startswith('C'):
                count += 1
    print("Number of lines not starting with 'C':", count)

count_non_c_lines(count_non_c_lines("d:\\pythonassignments\\python-module\\python-assignments\\Assignment7\\story.txt"))