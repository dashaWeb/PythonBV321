# student = {'name':'Stas','lastname':'Bondar','rating':11.8,'group':'PD322','birthdate':'13.11.06'}

# print(student,'\n')
# print(student['name'],student['rating'],'\n')


# for key in student.keys():
#     print(f'{key} --> {student[key]}')

# print()

# for value in student.values():
#     print('\t',value)

# print()

# for key,value in student.items():
#     print(f'{key} -->\t{value}')

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student,'\n')
# del student['rating']
# print(student,'\n')
# student.popitem()
# print(student,'\n')
# student.pop('lastname')
# print(student,'\n')

# student['email'] = 'stasbondar4532@gmail.com'

# print(student,'\n')
# students = [
#     {'name':'Stas1','lastname':'Bondar','rating':11.8,'group':'PD322','birthdate':'13.11.06'},
#     {'name':'Stas2','lastname':'Bondar','rating':11.8,'group':'PD322','birthdate':'13.11.06'},
#     {'name':'Stas3','lastname':'Bondar','rating':11.8,'group':'PD322','birthdate':'13.11.06','marks':[10,11,12,10]}
# ]
# print(students[2]['marks'])

# for i in students[2]['marks']:
#     print(i)
# import json


# obj = {'name':'Stas1','lastname':'Bondar','rating':11.8,'group':'PD322','birthdate':'13.11.06'}

# print(type(obj))
# print(obj,'\n')


# byte_obj = json.dumps(obj)
# print(type(byte_obj))
# print(byte_obj,'\n')


# new_obj = json.loads(byte_obj)
# print(type(new_obj))
# print(new_obj,'\n')
# with open('17_file/students.txt','w') as file:
#     file.write(str(obj))

# import json
# # obj = {'name':'Stas1','lastname':'Bondar','rating':11.8,'group':'PD322','birthdate':'13.11.06'}
# # with open('17_file/students.txt','w') as file:
# #     file.write(json.dumps(obj))
#     # print(info['name'])
# with open('17_file/students.txt') as file:
#     info = file.read()
#     print(info)
#     new_info = json.loads(info)
#     print(new_info['name'])


# import requests

# url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'

# result = requests.get(url).json()
# print(result)
# print(type(result))
# print(result[0]['sale'])

# url = 'https://static.vecteezy.com/system/resources/previews/002/376/764/original/beautiful-sunset-on-summer-background-free-vector.jpg'

# img = requests.get(url)
# with open('17_file/bg.jpg','wb') as file:
#     file.write(img.content)

# import requests
# url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&category=animals&colors=turquoise'

# res = requests.get(url).json()['hits']

# counter = 1
# for img in res:
#     with open(f'17_file/img/{counter}.jpg','wb') as file:
#         pictr = requests.get(img['webformatURL'])
#         file.write(pictr.content)
#     counter+=1

# fr_1 = {'num':4,'denum':6}
# fr_2 = {'num':3,'denum':9}

# def sum(one,two):
#     num = one['num'] * two['denum'] + two['num'] * one['denum']
#     denum = one['denum'] * two['denum']
#     return {'num':num,'denum':denum,'int':2}

# print(sum(fr_1,fr_2))





