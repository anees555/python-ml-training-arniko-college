# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# print the even number between 10 and 20 using continue statement
# for i in range(11, 20):
#     if i%2 != 0:
#         continue
#     print(i)

# prepare a table of a number uptp 10
# 9 * 1 = 9 to 9 * 10 = 90

num = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
