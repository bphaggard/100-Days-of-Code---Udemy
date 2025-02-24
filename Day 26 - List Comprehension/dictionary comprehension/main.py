import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Patrick"]
students_scores = {student:random.randint(1, 100) for student in names}
#print(students_scores)
passed_students = {student_p:student_s for student_p, student_s in students_scores.items() if student_s >= 60}
#print(passed_students)

#Exercises
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_sentence = sentence.split()
result = {word:len(word) for word in split_sentence}
#print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp * 9/5) + 32) for day, temp in weather_c.items()} #convert celsius to fahrenheit

#print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    #print(row.student)
    #print(row.score)
    if row.student == "James":
        print(row.score)