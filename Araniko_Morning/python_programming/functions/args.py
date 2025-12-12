# args and kwarg
# *args
# def my_func(*args):
#     print(f"My first argument: {args[0]}")
#     print(f"My second arguemnt: {args[1]}")
#     print(f"my third argumet: {args[2]}")

# my_func(45, 67, 89)

# def add_num(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# add_num()
# add_num(34)
# add_num(45, 56)
# add_num(67, 78, 90)
# add_num(34, 56, 78, 12, 43)

# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# my_function(name = "Something", address = "Biratnagar", Class = "XII", section = "Sun")

def my_function(*args, **kwargs):
    for i in args:
        print(i)
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function("Anish Dahal", city = "Biratnagar", state = "Koshi", country = "Nepal" )