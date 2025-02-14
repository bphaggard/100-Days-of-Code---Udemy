#READ file
with open("my_file.txt") as file: #Absolute file path "/Users/patrikmlcoch/Desktop/my_file.txt", Relative path "./my_file" for the current folder
    contents = file.read()
    print(contents)

#WRITE to file
# with open("my_file.txt", mode="a") as file: # mode "w" rewrite everything, "a" will append
#     file.write("\nnew text")