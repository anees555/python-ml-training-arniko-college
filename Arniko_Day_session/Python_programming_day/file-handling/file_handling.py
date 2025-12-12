### Creating a new file

# f = open("newfile1.txt", "x")
# print(f.name)
# print(f.mode)

### Writing a file
# f = open("newfile1.txt", "w")
# f.write("This is the first line i have written\n")
# f.write("This the second line i am written")
# f.close()
## Reading a file
# f = open("newfile1.txt", "r")
# content  = f.read()
# print(content)

# f = open("newfile1.txt", "a")
# f.write("\nThis is the recently added content")

# create a new file and write the contents on that file and copy that content to the next file

# with open("original_file.txt", "w") as f:
#     f.write("This is the content i want to copy it to the next file")

# with open("original_file.txt", "r") as f:
#     content = f.read()

# with open("copy_file.txt", "w") as f:
#     f.write(content)


### Binary file
with open("C:\\Users\\Lenovo\\Downloads\\cat_bw.jpeg", "rb") as f:
    content = f.read()
    print(content)

with open("copy_img.jpeg", "wb") as f:
    f.write(content)