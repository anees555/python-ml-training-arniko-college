# Error

# s = int("hello")
# print(s)

# print(43 + "45")

# print(34/0)

    # print("hello world")

# list1 = [23, 45, 67, 80]
# print(list1[4])

# Exception handling
# try:
    # code to be executed which may have error
# except:
    # Fallback statement
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    quotient = a / b
except ValueError:
    print("Exception occurred: Value Error")
except ZeroDivisionError:
    print("Exception occurred: ZeroDivisionError")
else:
    print(f"Quotient: {quotient}")
finally:
    print("Code executed successfully")




# list1 = ["123", "78", "hello", "56", "python", "100"]
# result = []
# for element in list1:
#     try:
#         result.append(int(element))
#     except:
#         result.append("Invalid")
# print(result)




