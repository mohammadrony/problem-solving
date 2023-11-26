f = 101
print(f)

def newFunction():
  global f
  print(f)
  f = "changing global variable"

newFunction()

print(f)
del f
print(f)
