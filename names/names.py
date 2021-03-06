import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BSTNode(names_1[0])

for name in names_1:
    bst.insert(name)
for name in names_2:
    bst.contains(name, duplicates)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# print(f"Length: {len(no_duplicates)}")
# print(f"{len(no_duplicates)} duplicates:\n\n{', '.join(no_duplicates)}\n\n")
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

my_duplicates = []
names = set(names_1).intersection(names_2)
for name in names:
    my_duplicates.append(name)

end_time = time.time()
print(f"{len(my_duplicates)} duplicates:\n\n{', '.join(my_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
