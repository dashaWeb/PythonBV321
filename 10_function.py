

# def showMessage(name):
#     print('Hello,',name)




# name_ = input('Enter name > ')

# showMessage(name_)
# showMessage('Igor')
# showMessage('Pasha')


# def sum(a,b):
#     # res = a+b
#     # return res
#     return a+b

# def sub(a,b):
#     return a - b
# def mult(a,b):
#     return a * b
# def div(a,b):
#     if b == 0:
#         return
#     return a / b


# def calculete(a,b,op):
#     if op == '+':
#         return sum(a,b)
#     if op == '-':
#         return sub(a,b)
#     if op == '*':
#         return mult(a,b)
#     if op == '/':
#         return div(a,b)

# def getOperation(line):
#     if line.find('+') != -1:
#         return '+'
#     if line.find('-') != -1:
#         return '-'
#     if line.find('*') != -1:
#         return '*'
#     if line.find('/') != -1:
#         return '/'

# reg = input('Enter Example (2+2) > ')
# op = getOperation(reg)
# numb1 = float(reg.split(op)[0])
# numb2 = float(reg.split(op)[1])

# res = calculete(numb1,numb2,op)
# print('Result :: ',res)
# import random
# def fillList(number,min=1,max=10):
#     return [random.randrange(min,max+1) for i in range(number)]


# numbers = fillList(10,20,50)

# print(numbers)

