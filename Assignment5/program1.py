#Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

people = {'arhan':'blue' , 'lisa':'yellow' , 'vinod':'purple' , 'jenny':'pink'}

number_of_students = len(people)
print("Number of students are:", number_of_students )

people['lisa'] = 'black'
print("Lisa's new fav clr:", people)

del people['jenny']
print("Updated list:", people)

for name in sorted(people):
    print(f"{name} : {people[name]}")