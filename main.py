import requests 
# import uuid
# from datetime import date, datetime, timedelta
# from pydantic import BaseModel, confloat, validator, field_validator
# from enums import DepartmentEnum
from models import Student, Module

# url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()
# print(data)

#testing inbuilt validation
# data.append(
#     {
#         "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
#         "name": "Eric Travis",
#         "date_of_birth": "1995-05-25",
#         "GPA": "6.2",
#         "course": "Computer Science",
#         "department": "Science and Engineering",
#         "fees_paid": False
#     }
# )

#Testing custom validation
# data.append(
#     {
#         "id": "48dda775-785d-41e3-b0dd-26a4a2f7722f",
#         "name": "Justin Holden",
#         "date_of_birth": "2010-08-22",
#         "GPA": "3.23",
#         "course": "Philosophy",
#         "department": "Arts and Humanities",
#         "fees_paid": 'true'
#     }
# )

#Testing enum functionality
# data.append(
#     {
#         "id": "48dda775-785d-41e3-b0dd-26a4a2f7722f",
#         "name": "Justin Holden",
#         "date_of_birth": "2010-08-22",
#         "GPA": "3.23",
#         "course": "Philosophy",
#         "department": "ABC",
#         "fees_paid": 'true'
#     }
# )

#Test Literal
# data[-1]['modules'].append(
#     {
#                 "id": 1,
#                 "name": "Data Science and Machine Learning",
#                 "professor": "Prof. Susan Love",
#                 "credits": 23,
#                 "registration_code": "abc"
#             },
# )

#test modules validator
# data[-1]['modules'].append(
#     {
#                 "id": 1,
#                 "name": "Data Science and Machine Learning",
#                 "professor": "Prof. Susan Love",
#                 "credits": 20,
#                 "registration_code": "abc"
#             },
# )



# for student in data:
#     # create Pydantic model object by unpacking key/val pairs from our JSON dict as arguments 
#     model = Student(**student)
#     print()
#     print(model)
    #Converting pydantic model to dictionary instance
    # print()
    # print("DICTIONARY")
    # print(model.dict())
    #Converting pydantic model to JSON
    # print()
    # print("JSON")
    # print(model.json())
    # for module in model.modules:
    #     print(module.id)

# print(Module.schema_json(indent=2))
print(Student.schema_json(indent=2))