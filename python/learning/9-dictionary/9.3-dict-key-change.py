sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

aD = {"location" if i == "city" else i: j for i, j in sample_dict.items()}

print(aD)
