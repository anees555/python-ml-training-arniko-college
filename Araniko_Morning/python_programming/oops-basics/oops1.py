# Procedural programming concept
# a = 56
# b = 34


# add = a + b

# subtract = a - b

# multiply = a * b

## Creating class

# class Student:
#     def __init__(self, name, roll, address):
#         print("I am called")
#         self.name = name 
#         self.roll = roll
#         self.address = address
    
#     def student_info(self):
#         print(f"Name: {self.name} | Address: {self.address} | Roll: {self.roll}")
    

# s1 = Student("Student_name", "007", "Biratnagar")
# print(s1.name, s1.address, s1.roll)
# s1.student_info()
# s2 = Student()
# s3 = Student()
# s4 = Student()
# print(s1.name)
# print(s2.name)

# Car class with properties brand, model number, Whether the car is EV or diesel car with methods: starts, stops, breaks and car info to print the attributes of the car

# class Parent:
#     hair_color = "Golden Brown"

# class Child(Parent):
#     pass

# child1 = Child()
# print(child1.hair_color)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"I am {self.name} and I am {self.age} year old.")

# class Student(Person):
#     def __init__(self, name, age, roll):
#         super().__init__(name, age)
#         self.roll = roll
#     def student_info(self):
#         print(f"I am {self.name}, i am student , my age is {self.age}, my roll number is {self.roll}")

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#             super().__init__(name, age)
#             self.subject = subject

#     def teach(self):
#             print(f"I teach {self.subject}")

# ## Creating object
# s1 = Student("Ram", 30, "007")
# t1 = Teacher("Sujan", 40, "Math")
# s1.student_info()
# s1.introduce()
# t1.teach()


# #### 
# class Student:
#     def __init__(self): ### constructor
#         print("I am called")
#         print(self)


# s1 = Student()
# print(s1)
# s2 = Student()
# print(s2)
# # # __init__() # no need call , call automatically at the time of object creation



class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_sum(self):
        print(f"The sum is {self.a + self.b}")

s1 = Sum(34, 56)
s1.calculate_sum()