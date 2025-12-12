# # list1 = [1, 2, 3, 4, 5]
# # print(type(list1))
# # print(list1)

# # list2 = [23, 45, "hello", "python", True]
# # # print(type(list2))
# # # print(list2)
# # # print(list2)
# # # list2[3] = "Java"
# # # print(list2)

# # # empty_list = []
# # # empty_list1 = list()

# # # # print(empty_list)
# # # # print(empty_list1)

# # # # append function 
# # # empty_list.append("hello")
# # # empty_list.append("python")
# # # empty_list.append("program")
# # # print(empty_list)

# # list2 = [34, 56, 78]
# # list2.insert(2, 100)
# # # print(list2)
# # list2.remove(56)
# # # print(list2)

# # list2.extend([34, 78])
# # # print(list2)

# # # list2.
# # # for i in list2:
# # #     print(i)

# # print(list2)
# # print(len(list2))
# # ## ask the user to enter  the 5 number and create the list

# # number_list = []
# # count = 0
# # while count < 5:

# #     n = int(input("Enter the number: "))
# #     number_list.append(n)
# #     count += 1
# # print(number_list)
# # number_list.append(n)

# # create list with 5 number and perform the square of each number and store in another list
# numbers = [1, 3, 5, 6, 8]
# square = []

# for i in numbers:
#     # print(i)
#     i = i**2
#     square.append(i)
# # print(square)

# # print(square)
# # print(square[1:3])
# # list1 = [1, 2, 3, 4]
# # list2 = [4, 5, 6, 8]
# # print(list1 + list2)

# tuple_1 = (1, 2, 3, 4, 5) # immutable
# list_1 = [1, 2, 3, 4, 5] # mutable

# # tuple_1[1] = 8
# # print(tuple_1)

# # list_1[1] = 8
# # print(list_1) 

# # packing
# my_tuple = 1, 3, 4
# print(my_tuple)

# unpacking
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# list1 = [1, 3, 5, 6]
# # tuple1  = tuple(list1)
# # print(tuple1)

# list1.sort()
# print(list1)

# Set in python 
# set1 = set()
# print(type(set1))
# set1 = {1, 3, 4, 5, 6, 8, 9, 3, 5, 3}
# print(set1)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 7, 8, 9}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.isdisjoint(set2))

# set1.intersection_update(set2)
# print(set1)

# print(set1.add(34))
# print(set1)
# set1.add(34)
# print(set1)
# set1.remove(3)
# print(set1)

# set2 = {1, 2, 4, (6, 7, 8), 10}
# # set3 = {1, 2, 4, [6, 7, 8], 10}

# print(set2)
# # print(set3)

# dictionary

dict1 = {
    "Name": "Something",
    "Address": "Biratnagar",
    "Roll No": "007",
    "Class": "XII",
    "Marks": [45, 56, 78, 98]
}

# print(dict1)
# print(type(dict1))

# print(list(dict1.keys()))
# print(list(dict1.values()))
# print(list(dict1.items()))

# accessing the value in the dictionary
# dict1["Address"] = "Pokhara"
# print(dict1)

# # loop in dictionary
# # for i in dict1.keys():
# #     print(i)

# # for i in dict1.values():
# #     print(i)

# # for i, j in dict1.items():
# #     print(f"{i} : {j}")
# parent_dict = {
#     1: {
#         "Name": "Something",
#         "Address": "Brt",
#         "Class": "XII"
#     },
#     2: {
#         "Name": "Something1",
#         "Address": "Brt",
#         "Class": "XI"
#     }
# }

student = {
	"Student1": {
    	"name": "Ram",
        "Section": "Sun",
        "Roll": "007"
        },
    "Student2": {
    	"name": "Syam",
        "Section": "Moon",
        "Roll": "008"
        }
    }
# for x, y in student.items():
# 	print(x)
# 	for z in y:
# 		print(f"{z}: {y[z]}")

# print(student["Student1"]["name"])



