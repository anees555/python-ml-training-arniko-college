# Procedural programming concept
# a = 56
# b = 34


# add = a + b

# subtract = a - b

# multiply = a * b


# class Student:
#     ### contructor
#     def __init__(self, name, age, roll):
#         # print("I am called")
#         # print(self)
#         self.name = name  
#         self.age = age
#         self.roll = roll
    
#     def student_info(self):
#         print(f"Name of student is {self.name}, age is {self.age} and roll number is {self.roll}")

# s1 = Student("Ram", 30, "007")
# s1.student_info()
# # s1 vanne ko object ko name k hola?
# # print(s1.name)
# # print(s1.roll)
# # print(s1)
# # s2 = Student()
# # s3 = Student()

# # s4 = Student()

# # s5 = Student()









# # s1 = Student()
# # print(s1.name, s1.age)

# # s2 = Student()
# # print(s2.name, s2.age)

# # s3 = Student()
# # print(s3.name, s3.age)

### Inheritance 

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
#     def info(self):
#         print(f"My name is {self.name} and I am {self.age} year old")

# class Student(Person):
#     def __init__(self, name, age, roll):
#         super().__init__(name, age)
#         self.roll = roll

#     def student_info(self):
#         print(f"I am student. My roll no. is {self.roll}")

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#     def teach(self):
#         print(f"I am a teacher, I teach {self.subject}")

# s1 = Student("Ram", 24, "007")
# s1.student_info()
# s1.info()

# t1 = Teacher("Sujan", 45, "Math")
# t1.teach()
# t1.info()


# class Student:
#     def __init__(self, name):
#         self.name  = name

# class Man(Student):
#     def __init__(self, name):
#         super().__init__(name)


# s1 = Man()
# print(s1.name)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Cart:
    def __init__(self):
        self.product = []
    
    # def show_cart(self):
    #     for item in produc:
    #         print(item.name)
    
    def add_product(self)