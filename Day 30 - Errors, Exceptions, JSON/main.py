#File Not Found
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key222"])
except FileNotFoundError:
    file = open("a_file.txt", "w") #if file does not exist, it will create it
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read() #it will execute only if try block has no errors
    print(content)
finally:
    file.close() #this always proceed even if try block has some error
    print("File was closed")

#Our own error exception with raise
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)