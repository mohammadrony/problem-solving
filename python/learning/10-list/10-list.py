user = ['rony', 'imran', 'shanto']
print(user[0:2])

user.insert(1, 'rony')
print(user)

user.remove('rony')
print(user)

newusers = [['user1'], ['user2']]
user.extend(newusers)

newset = {'first', 'second'}

print(newset)

user.extend(newset)

print(user)

user.clear()
print(user)
