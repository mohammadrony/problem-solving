import math


def prime_factors(n):
    factors = []
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1

    if n > 1:
        factors.append(int(n))

    return factors


def get_common(arr1, arr2):
    i, j = 0, 0
    common = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            common.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return common


num1, num2 = 225, 100
factors1 = prime_factors(num1)
factors2 = prime_factors(num2)
commons = get_common(factors1, factors2)

gcd = 1
for i in commons:
    gcd *= i

print(
    "GCD of "
    + str(num1)
    + " and "
    + str(num2)
    + " = "
    + str(gcd)
    + ". (Using regular math operations)."
)

# print([value for value in factors1 if value in factors2])
