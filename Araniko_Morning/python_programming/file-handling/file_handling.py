# f = open("file_path", "mode")
## creating a file 
# file_path = "newfile.txt"
# f = open(file_path, "x")
# print(f.name)
# print(f.mode)

## writing something in the file
# f = open("newfile.txt", "w")
# f.write(f"Hello, this is the first line\n")
# f.write(f"Hello, this is the second line\n")
# f.wri
# 
# te(f"Hello, this is the third line\n")
# f.close()


# f = open("newfile.txt", "r")
# # data = f.read()
# # print(data)
# # line1 = f.readline()
# # line2 = f.readline()
# # print(line1)
# # print(line2)
# lines = f.readlines()
# print(lines)


# line1 = f.readline(1)
# print(line1)

# with open("newfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# to append something in the file
# with open("newfile.txt", "a") as f:
#     f.write("This is the recently added content")

# To copy the content from one file to another file
# creating new file for write
# with open("newfile.txt", "r") as f1:
#     content = f1.read()

# with open("note.txt", "w") as f2:
#     f2.write(content)


# Prepare the file to store the grade and scores of the students by calculating the percentage and grade 

def calculate_score():
    phy = float(input("Enter the marks of physics: "))
    chemi = float(input("Enter the marks of chemistry: "))
    math = float(input("Enter the marks of math: "))

    percent = (phy + chemi + math)/3 
    return phy, chemi, math, percent

def calculate_grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    elif percent >= 50:
        return "E"
    else:
        return "Fail, can't calculate grade"
def main():
    name = input("Enter the name of student")
    roll = input("Enter the roll number: ")
    phy, chemi, math, score = calculate_score()
    grade = calculate_grade(score)
    
    with open("student.txt", "a") as f:
        f.write(f"--------RESULT---------\n")
        
        f.write(f"Name: {name}\n")
        f.write(f"Roll No: {roll}\n")
        f.write("-------- Marks --------\n")
        f.write(f"physics: {phy}\n")
        f.write(f"Chemistry: {chemi}\n")
        f.write(f"Math: {math}\n")
        f.write("---------Final Score-------\n")
        f.write(f"Percentage: {score}\n")
        f.write(f"Grade: {grade}\n")
    
main()

    




