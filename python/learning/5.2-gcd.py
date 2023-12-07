a, b = 22, 18

a1, b1 = a, b

while b != 0:
    c = b
    b = a % b
    a = c

print("GCD of " + str(a1) + " and " + str(b1) + " = " + str(a) + ".")
