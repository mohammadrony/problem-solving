import array
num = array.array('i', [1, 2, 3, 4, 5, 6])

num[0] = 10
print(num)

num[1:4] = array.array('i', [4, 6, 8])
print(num)