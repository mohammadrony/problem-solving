list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)

res = [x + y for x, y in zip(list1, list2)]
print(res)

for i in (x + y for x, y in zip(list1, list2)):
    print(i)
