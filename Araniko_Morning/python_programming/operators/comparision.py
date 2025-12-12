# a = 56
# b = 56
# print(a == b)

# c = 45
# d = 54
# print(d > c)

# name = "Anish Dahal"
# length_of_name = len(name)
# print(length_of_name)


password = input("Enter your password: ")
min_len = 8
max_len = 20
default_password = "12345678"


is_longer = len(password) > min_len
is_not_default = (password != default_password)
is_shorter_than_max = len(password) < max_len

print(f"The entered password is longer?: {is_longer}")
print(f"The entered password is not default?: {is_not_default}")
print(f"The entered password is not longer than max?: {is_shorter_than_max} ")
