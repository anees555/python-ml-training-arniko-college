
# s = int("hello")
# print(s)

# a = 45
# b = '123'
# print(a + b)

# a = 45
# b = 0
# print(a / b)

# try:
    # risky code
# except:
    # fall back statement
# finally:
    # runs code anyhow

# try:
#     s = int("hello")
#     print(s)
#     print(type(s))
# except:
#     print("Exception occurred!")
# finally:
#     print("Code ended")

# write a program to ask the two number from user and perform division operation
# try:
#     num1 = int(input('Enter the first number: '))
#     num2 = int(input("Enter the second number: "))

#     division = num1 / num2

# except ValueError:
#     print("Value error occured!")
# except TypeError:
#     print("Type error occured")
# except ZeroDivisionError:
#     print("Zero division error occurred")
# else:
#     print(division)
# finally:
#     print("Program ended")

# list1 = [12, "hello", 45]

# try:
#     print(list1[3])
# except IndexError:
#     print("Index is out of range")

list1 = ["123", "45", "34", "hello", "python", "100"]
# Convert the each element of the list to integer if compatible otherwise replace the incompatible element with word "Invalid"
converted_list = []

for element in list1:
    try:
        converted_list.append(int(element))
    except ValueError:
        converted_list.append("Invalid")
print(converted_list)



