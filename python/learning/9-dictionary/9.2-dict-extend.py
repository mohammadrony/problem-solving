dict1 = {"name": "rony", "roll": 29}
dict2 = {"age": {'what': 23, 'again': 24}}

dict1.update(dict2)
print(dict1)

if(29 in dict1.values()):
    print('29 in the dict')