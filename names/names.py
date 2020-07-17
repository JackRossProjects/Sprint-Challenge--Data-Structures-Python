import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''


# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
# Above runtime = 10.09481143951416 seconds
# Above runtime complexity = O(n^2) || O(n) because the loop executes n times,
#                                      O(n^2) because the loop is nested.

'''
I think we can use a binary search tree for this problem because
python assigns numeric values to different letters as shown below:

a = 'a'
b = 'b'

if a > b:
    print("true")
else:
    print("false")

We should be able to use the first letter of the name to determine
where each name should be in a binary search tree.
'''

duplicates = []  # Return the list of duplicates in this data structure
binary_search_tree = BSTNode("root")

for name_1 in names_1:
    binary_search_tree.insert(name_1)

for name_2 in names_2:
    if binary_search_tree.contains(name_2):
        duplicates.append(name_2)

# Improved runtime = 0.25955724716186523 seconds
# Improved runtime complexity = O(2n) || 2n because 2 loops execute n times

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
