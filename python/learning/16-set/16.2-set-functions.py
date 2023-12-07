# 1
print("-------------------------------------------------------------------")
print("Exercise 1: Add a list of elements to a set")
print("-------------------------------------------------------------------")
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

# 2
print("-------------------------------------------------------------------")
print("Exercise 2: Return a new set of identical items from two sets")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1 & set2
print(set3)

# 3
print("-------------------------------------------------------------------")
print("Exercise 3: Get Only unique items from two sets")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1 | set2
print(set3)

# 4
print("-------------------------------------------------------------------")
print("Exercise 4: Update the first set with items that don’t exist in the second set")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set3 = set1 - set2
print(set3)

# 5
print("-------------------------------------------------------------------")
print("Exercise 5: Remove items from the set at once")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}
print(set1 - set2)

# 6
print("-------------------------------------------------------------------")
print("Exercise 6: Return a set of elements present in Set A or B, but not both")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 ^ set2)

# 7
print("-------------------------------------------------------------------")
print(
    "Exercise 7: Check if two sets have any elements in common. If yes, display the common elements"
)
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1 & set2)

# 8
print("-------------------------------------------------------------------")
print("Exercise 8: Update set1 by adding items from set2, except common items")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 ^ set2)

# 9
print("-------------------------------------------------------------------")
print("Exercise 9: Remove items from set1 that are not common to both set1 and set2")
print("-------------------------------------------------------------------")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 & set2)
