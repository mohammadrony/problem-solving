# Sets are unordered, so you cannot be sure in which order the items will appear.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1)

print(set1.union(set2))

print(set1.difference(set2))
# set1.difference_update(set2)
# print(set1)
# set1.difference_update({10, 20, 30})
# print(set1)

print(set1.symmetric_difference(set2))
# set1.symmetric_difference_update(set2)
# print(set1)


if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))
