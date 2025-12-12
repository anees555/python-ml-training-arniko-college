# number = int(input("Enter the number to check even"))

# if number % 2 == 0:
#     print("The number is even.")
# print("The number is checked succesfully")

# write a program to ask the name of the user and print the greeting statement only if user enter the name otherwise do nothing

# name = input("Enter the name: ")

# if name: 
#     print(f"Hello {name}, How are you?")

# write a program to calculate the actual amount to be paid by deducting the discount using discount rate only if the total amount is greater than 1000, otherwise just print the output as "Thankyou for shopping!"
# total_amount = float(input("Enter the total amount: "))

# if total_amount > 1000:
#     discount_rate = 0.10
#     actual_amount = total_amount - (total_amount * discount_rate)
#     print(f"Your actual amount to be paid is : {actual_amount}")

# else:
#     discount_rate = 0.05
#     actual_amount = total_amount - (total_amount * discount_rate)
#     print(f"Your actual amount to be paid is : {actual_amount}")



# print("Thankyou for shopping!")

# number = int(input("Enter the number to check: "))

# if number > 0:
#     print("The number is positive")

# elif number < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# Write a program to print the maximum number from the 3 numbers
# a = 34
# b = 43
# c = 21

# if (a>b) and (a>c):
#     print("a is maximum")
# elif (b > a) and (b>c):
#     print("b is maximum")
# else:
#     print("c is maximum")

# program to check number is negative or positive or zero
number = int(input("Enter the number to check: "))

if number >= 0:
    if number == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")