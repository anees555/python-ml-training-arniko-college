# a = 45
# b = 56
# print(a>b)

# password check garne task
# ask user to input password
# set the minimum length of password using min_len variable
# check whether the length of password is greater than min_len or not


# name =  "Python programming"
# lenght_of_name = len(name)
# print(lenght_of_name)

password = input("Enter your password: ")

min_len = 8
default_password = "12345678"
max_len = 16

is_greater_than_min_len = len(password) > min_len

is_shorter_than_max_len = len(password) < max_len

is_not_default = password  !=  default_password

print(f"Is password longer than minimum length: {is_greater_than_min_len}")
print(f"Is password not default: {is_not_default} ")
print(f"Is password shorter than maximum length: {is_shorter_than_max_len}")

