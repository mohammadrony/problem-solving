string1 = input("Your first string : ")
string2 = input("Your second string : ")
string3 = input("Your third string : ")

string = string1[0:3] + string3[0:3] + string2[0:2]

print("Your password is : " + string)

i = 0

print("lower case characters: ", end="")

for char in string:
    if char >= "a" and char <= "z":
        print(char, end=", ")
print()

print("upper case characters: ", end="")

for char in string:
    if char >= "A" and char <= "Z":
        print(char, end=", ")
print()

print("other characters: ", end="")

for char in string:
    if (char < "a" or char > "z") and (char < "A" or char > "Z"):
        print(char, end=", ")
print()
