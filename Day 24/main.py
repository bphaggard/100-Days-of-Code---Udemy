#READ file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#WRITE to file
with open("my_file.txt", mode="a") as file: # mode "w" rewrite everything, "a" will append
    file.write("\nnew text")