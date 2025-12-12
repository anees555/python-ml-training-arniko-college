# 
# a = 10
# if a > 0:
#     print("a is greater than zero")

# ask user to input your name
# excute the block only if you enter your name 
# print output like this "Hello (name)! How are you?"
# otherwise  do nothing
# name = input("Enter your name: ")

# if name:
#     print(f"Hello {name}, How are you?")

# ask user to input the amount to be paid
# if amount is greater than 1000, compute the discount and calculate the actual amount to be paid otherwise just print amount 

amount = float(input("Enter the total amount: "))

if amount > 1000:
    discount_rate = 0.10
    discount_amount = discount_rate * amount
    amount -= discount_amount
    print(f"Actual amount to be paid: {amount}")

print("Thankyou for shopping")