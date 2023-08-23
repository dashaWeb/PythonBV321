# import json

# def createItem():
#     id = int(input('Enter id > '))
#     name = input('enter name > ')
#     return {'id':id,'name':name}

# def createList(number):
#     users = []
#     for i in range(number):
#         users.append(createItem())
#     return users

# def writeUsers(data):
#     with open('data.json','w') as file:
#         file.write(json.dumps(data))

# def readUsers():
#     with open('data.json') as file:
#         return json.loads(file.read())

# while True:
#     choice = int(input('''
#                     1 - Fill DB
#                     2 - Add User;
#                     3 - Delete User;
#                     4 - Print User;
#                     5 - sort Users
#                     0- exit
#                     '''))
#     if choice == 1:
#         number = int(input('Enter number of users'))
#         users = createList(number)
#         writeUsers(users)
#     if choice == 2:
#         users = readUsers()
#         users.append(createItem())
#         writeUsers(users)
#     if choice == 0:
#         break

list_ = [
    {"id": 12, "name": "sasha"},
    {"id": 3, "name": "Masha"},
    {"id": 1, "name": "Olya"},
    {"id": 3, "name": "Olya"},
    {"id": 1, "name": "olya"},
    {"id": 3, "name": "Olya"},
]


def printUser(data):
    for i in range(len(data)):
        print(i+1,data[i])

printUser(list_)
print('*'*40)
# list_.sort(key = lambda x: str.lower(x['name']))
# list_2  = sorted(list_,key = lambda x: x['id'])

# list_2 = list(filter(lambda x:x['id'] == 3,list_))
# list_2 = list(filter(lambda x:x['name'] == "Olya",list_))
list_2 = list(map(lambda x:{"id": x['id'] + 2, "name": x['name']},list_))

printUser(list_2)