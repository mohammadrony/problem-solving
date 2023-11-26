from typing import TypeVar, Type

T = TypeVar("T", str, complex, float, int)

def fun(t: Type[T]) -> T:
    return t(42)

print("fun(int)\t\t" + str(type(fun(int))) + "\t- " + str(fun(int)))
print("fun(float)\t\t" + str(type(fun(float))) + "\t- " + str(fun(float)))
print("fun(complex)\t" + str(type(fun(complex))) + "\t- " + str(fun(complex)))
print("fun(str)\t\t" + str(type(fun(str))) + "\t- " + str(fun(str)))