car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

key = car.keys()
val = car.values()
data = car.items()

for item in data:
    print(type(item))

print(key)
print(val)
print(data)
for i in car:
    print(i)
    print(car[i])
