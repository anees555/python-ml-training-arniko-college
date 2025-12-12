# basic understanding of the function

# def func1():
#     # code implementation here
#     print("Hello python programmer")

# func1()
# # perform other task implementation
# # perform other task implementation

# # perform other task implementation

# # perform other task implementation

# # perform other task implementation

# func1()

# parameters in function

# def func2(name, age): # parameters passing
#     print(f"Hello {name}")
#     print(f"You are {age} year old")

# func2("Ram", 30) # argument passing
# func2("Shyam", 32)

# write a program to add two number using function

# def sum_calculate(a, b):
#     sum = a + b
#     print(sum)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# sum_calculate(num1, num2)


# # return statement
# def sum_number(num1, num2):
#     return num1 + num2

# # print(sum_number(23, 45))

# sum_result = sum_number(23, 45)
# print(sum_result)

# write a program to perform sum, difference, product, and division using single return statement and store the value back to corresponding variables: sum, difference, product and division

# def calculate(num1, num2):
#     return num1 + num2, num1 - num2, num1 * num2, num1 / num2

# result = calculate(45, 9)
# print(result)

# sum, difference, product, division = result
# print(f"Sum: {sum}")
# print(f"Difference: {difference}")
# print(f"Product: {product}")
# print(f"Division: {division}")

## Default aruguments

# def my_function(country = "Nepal"):
#     print(f"I am living in {country}")

# my_function()
# my_function("USA")
# # my_function("Britain")

# def add_number(a = 100, b=78):
#     return a + b

# sum = add_number(50, 10)
# print(sum)

# write a program to perform addition, substraction, multiplication, division using multiple function and ask the user for the numbers and operators to be performed in main function and display the output

def addition(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    op = input("Enter the operator to be used:(+, -, *, /): ")
    if op == '+':
        sum = addition(num1, num2)
        print(f"Sum: {sum}")

    elif op == '-':
        difference = substraction(num1, num2)
        print(f"Difference: {difference}")
    
    elif op == '*':
        product = multiplication(num1, num2)
        print(f"Product: {product}")

    elif op == '/':
        quotient = division(num1, num2)
        print(f"Quotient: {quotient}")
    
    else:
        print("Invalid operators")
    
main()

    


