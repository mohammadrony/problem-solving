sample_dict = {"Physics": 82, "Math": 65, "History": 75}

min1 = sample_dict.values()
print(min(sample_dict, key=sample_dict.get))
print(min(min1))
