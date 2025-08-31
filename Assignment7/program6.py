#Write a function in Python to count and display the total number of words in a text file.
#Note: use above "story.txt" file

def count_words_in_file(filename):
    try:
        with open("d:\\pythonassignments\\python-module\\python-assignments\\Assignment7\\story.txt", 'r') as file:
            text = file.read()
            words = text.split()
            print("Total number of words:", len(words))
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print("An error occurred:", e)

count_words_in_file("d:\\pythonassignments\\python-module\\python-assignments\\Assignment7\\story.txt")        