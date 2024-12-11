student_scores = [150, 142, 185, 120, 171,  184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#TOTAL SUM number function/for loop
total = sum(student_scores)
total_score = 0
for score in student_scores:
    total_score += score
print(total_score)

#MAXIMUM number function/for loop
max(student_scores)
maximum_number = 0
for number in student_scores:
    if maximum_number < number:
        maximum_number = number
print(maximum_number)

#MINIMUM number function/for loop
min(student_scores)
minimum_number = max(student_scores)
for number in student_scores:
    if number < minimum_number:
        minimum_number = number
print(minimum_number)

#TOTAL SUM from range 1-100
total_range = 0
for number in range(1, 101):
    total_range += number
print(total_range)

#FizzBuzz Game
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)