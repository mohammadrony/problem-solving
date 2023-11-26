import random

arr1 = [random.randint(1,20) for i in range(10)]
arr2 = random.sample(range(10, 15), 5)
arr3 = [random.randrange(30, 39, 2) for i in range(10)]
print(arr1)
print(arr2)
print(arr3)
