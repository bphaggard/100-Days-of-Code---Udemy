"""
PascalCase - for class
camelCase
snake_case
"""

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #Default value
        self.following = 0

    def follow(self, user): #follow is method
        user.followers += 1
        self.following += 1

user_1 = User("001", "Patrik")
user_2 = User("002", "Zuzka")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# print(user_1.username)
# print(user_1.id)
# print(user_1.followers)



# user_1 = User() #Object is user_1
# user_1.id = "001"
# user_1.username = "Patrik" #id and username are attributes (variable associated with an object)
#
# print(user_1.username)