def outer_fun(a, b):
    str1= 'google'
    print(a)
    def inner_fun(c, d, str1):
        return c + d

    return inner_fun(a, b, str1)
    return a

result = outer_fun(5, 10)
print(outer_fun(3, 2))
print(result)

def display_person(**args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")
