
# program to count up to 10
# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# for i in range(70, 80):
#     if i % 2 == 0:
#         continue
#     print(i)

# write a program to perform the factorial of the given input number
num = int(input("Enter the number to calculate: "))
# perform the conditional statement
if num < 0:
    print("No factorial for negative number")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1")
    

else:
    factorial_result = 1
    for i in range(1, num + 1):
        factorial_result = factorial_result * i
    print(factorial_result)