def get_gcd(a, b):
    if b == 0:
        return a

    return get_gcd(b, a % b)


print(get_gcd(110, 20))
