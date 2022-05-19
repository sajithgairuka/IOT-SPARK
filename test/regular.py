# Python3 code to demonstrate
# Prefix Separation
# Using list comprehension + startswith()
#https://www.geeksforgeeks.org/python-filter-list-elements-starting-with-given-prefix/
# initializing list
test_list = ['sapple', 'orange', 'smango', 'grape']

# initializing start Prefix
start_letter = 's'

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + startswith()
# Prefix Separation
with_s = [x for x in test_list if x.startswith(start_letter)]
without_s = [x for x in test_list if x not in with_s]

# print result
print("The list without prefix s : " + str(without_s))
print("The list with prefix s : " + str(with_s))
