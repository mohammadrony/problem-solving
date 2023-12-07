try:
    print("hello")
except:
    print("error")
else:
    print("hi")

try:
    v = None
    arr = [1, 2]
    print(arr[3])
    print("Hello" + v)
    print(2 / 0)
except IndexError:
    print("index out of bound")
except TypeError:
    print("Something went wrong")
except NameError:
    print("Something went wrong")
except ZeroDivisionError:
    print("can't devide by zero")
else:
    print("Nothing went wrong")
finally:
    print("Done")

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

try:
    x = -3
    print(x)
except:
    print("error")
