# - Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

given_list= ['a', 'b', 'c', 'd', 'e']

index = given_list.index('b')

given_list[index:index+1] = [1, 2, 3]

print("Updated list:", given_list)