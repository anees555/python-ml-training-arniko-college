### Creating a file
# with open("newfile1.txt", "x") as f:
#     print(f.name, f.mode)

### Writing a file
# with open("newfile1.txt", "w") as f:
#     f.write("This is the file i have created recently\n")
#     f.write("This is the second line of this file")

# appending the file
# with open("newfile1.txt", "a") as f:
#     f.write("\nThis is the recently added line")

# reading a file
# with open("newfile1.txt", "r") as f:
#     data = f.read()
#     print(data)

## reading a binary file
with open("C:\\Users\\Lenovo\\Downloads\\cat_bw.jpg", "rb") as f:
    data = f.read()
    # print(data)

with open("copy_image.jpg", "wb") as f:
    f.write(data)



