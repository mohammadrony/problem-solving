# users = ['rony', 'md']
# role = {"designation": 'Developer', "salary": 8000}

# output = dict.fromkeys(users, role)
output = {
    "rony": {"designation": "Developer", "salary": 100},
    "md": {"designation": "Developer", "salary": 100},
}

print(output)
print(output["rony"].pop("salary"))
print(output)
