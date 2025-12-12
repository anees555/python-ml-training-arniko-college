# defining the function

# def first_func():
#     print("Hello python programmer")

# first_func()

# # number of task
# first_func()
# first_func()
# first_func()

# parameters
# input of the function for the functional block execution

# def second_func(name, age): # parameters
#     print(f"Hello {name}!")
#     print(f"You are {age} year old")

# second_func("Ram", 45) # arguments

# sum two number and print the result using function
# def sum_number(num1, num2):
#     sum = num1 + num2
#     print(sum)

# sum_number(34, 56)

# return statement

# def sum_num(num1, num2=45):
#     return num1 + num2

# print(sum_num(100))

# sum = sum_num(34, 67)
# print(sum)

# write a program to perform addition, -, *, / using one return statement and store results back to specific variables like sum, difference, product, division


# def calculate(a, b):
#     return a + b, a - b, a * b, a / b

# result = calculate(45, 5)
# print(result)

# sum, difference, product, division = result
# print(f"Sum: {sum}")
# print(f"Difference: {difference}")
# print(f"Multiply: {product}")
# print(f"Division: {division}")

# def list_len(list1):
#     # print(len(list1))
#     for i in list1:
#         print(i)

# list_len([1, 4, 6, 7, "hello", "python", "student", "1234"])


# Create a multiple function for addition, subtraction, multiplication and division and ask the user to perform which operation to be done and do the task as per user input

def addition(a, b):
    return a + b
def subtraction(a ,b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    op = input("Enter which operation to be used(+, -, *, /): ")

    #conditional statement here
    if op == '+':
        sum = addition(num1, num2)
        print(f"Sum: {sum}")
    elif op == '-':
        difference = subtraction(num1, num2)
        print(f"Difference: {difference}")

    elif op == '*':
        product = multiplication(num1, num2)
        print(f"Product: {product}")
    elif op == '/':
        quotient = division(num1, num2)
        print(f"Quotient: {quotient:.3f}")
    else:
        print("Invalid operation")

main()

# Write a program using multiple function to calculate the grade of the student, first function to ask the user about the score of the student, 2nd to check whether the user is pass or fail (if score > 50: pass otherwise fail), and if pass , another function to calculate the grade of the passed student and display the detail using the last main function






