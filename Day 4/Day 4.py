import random
import my_module

# number = random.randint(1, 10)
# print(number)
# print(my_module.my_favourite_number)

# random_number = random.random() #number between 0 - 1
# print(random_number)

# random_float = random.uniform(1, 10)
# print(random_float)

# words = ["Heads", "Tails"]
# random_value = random.randint(0,1)
# print(words[random_value])

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_person = random.randint(0, len(friends) - 1)
print(f"Bill will pay {friends[random_person]}")
#OR
print(f"Bill will pay {random.choice(friends)}")