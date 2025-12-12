# dict1 = {}
# print(type(dict1))
# print(dict1)

# data are structured in key value pair
# key = value
# dictionary book -> word and its corresponding meanings

dict1 = {
    "Name": "Sayapatri Group",
    "Address": "Biratnagar",
    "Work": "IT company"
}
# print(dict1)
# print(dict1["Name"])
# print(dict1["Address"])
# print(dict1["Work"])

# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# nested dictionary
# dictionary inside dictionary
# student = {
#     "student1": {
#         "Name": "Name of student1",
#         "Section": "Sun",
#         "Roll": "007",
#         "Marks": [23, 45, 56, 78]
#     },
#     "Student2": {
#         "Name": "Name of student2",
#         "Section": "Moon",
#         "Roll": "008",
#         "Marks": [45, 67, 78, 43]
#     },
#     "Student3": {
#         "Name": "Name of student3",
#         "Section": "Star",
#         "Roll": "010",
#         "Marks": [34, 54, 65, 90]
#     }
# }


student = {
    "Name": "Something",
    "Section": "Sun",
    "Roll": "007",
    "Marks": [45, 67, 89, 90]
}

# print(student)
# iterate through the keys
# for i in student.keys():
#     print(i)

# iterate through through values
# for i in student.values():
#     print(i)

# iterate through key value pair
# for i, j in student.items():
#     print(f"{i} = {j}")

# print(student)

# to update the value of the key
# student["Section"] = "Moon"
# print(student)

student.update({"Section": "Star"})
print(student)