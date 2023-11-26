list1 = ["hel", "wo"] 
list2 = ["lo", "rld", "!"]
list3 = [i + j for i, j in zip(list1, list2)]
# list3 = [i + j for i, j in zip(range(9), range(10,19))]

print(list3)