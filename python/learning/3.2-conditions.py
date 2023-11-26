val = 100
print(str(val) + " > 50 and " + str(val) + " < 200 = " + str(val > 50 and val < 200))
print(str(val) + " < 50 or " + str(val) + " > 200 = " + str(val < 50 or val > 200))
print("not " + str(val) + " < 200 = " + str(not val < 200))

if(val > 10 and not val > 1000):
    print('hey there!!')
