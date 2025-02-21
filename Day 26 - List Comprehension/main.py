# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers) #[2, 3, 4]

range_list = [r * 2 for r in range(1, 5)]
print(range_list)

#without comprehension
new_list = []
for n in numbers:
    new_list.append(n + 1)
print(new_list)

#conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Patrick"]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)

with open("file1.txt") as num1, open("file2.txt") as num2:
    numbers_1 = [int(nums.strip()) for nums in num1]
    numbers_2 = [int(numbs.strip()) for numbs in num2]
result = [nmb1 for nmb1 in numbers_1 if nmb1 in numbers_2]

print(result)