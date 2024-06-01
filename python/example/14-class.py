class User:
    def __init__(self, user_email, user_password):
        self.email = user_email
        self.password = user_password

    def get_email(self):
        return self.email

    def check_password(self, new_password):
        if new_password == self.password:
            return True
        else:
            return False


user1 = User("user1@email.com", "12345678")
user2 = User("user2@email.com", "abcdefgh")

print(user1.get_email())
print(user2.check_password("12345678"))
print(user1.email)
