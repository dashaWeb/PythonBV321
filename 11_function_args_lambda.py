
# def sumAllNumbers(start,end,*args):
#    print(start,end,args)
#    return sum(args)

# print(sumAllNumbers(1,4,5))


# def sum(a,b):
#     return a+b
# def show(color):
#     print(color)

# print(sum(2,5))
# show('red')

# lambda_show = lambda color:print(color)

# lambda_show('green')

# lambda_sum = lambda a,b:a+b
# print(lambda_sum(5,2))

# numbers = [4,5,8,7,4,1,2,5,6,9,3,2,5,4]

# def doubleList(list):
#     tmp = []
#     for item in list:
#         tmp.append(item * 2)
#     return tmp
# print(numbers)
# newNumbers = doubleList(numbers)
# print(newNumbers)

# line = input('Enter numbers :: ').split()
# line = [int(item) for item in line]
# print(line)


# numbers = [4,5,8,7,4,1,2,5,6,9,3,2,5,4]
# res = list(map(lambda x:x**2,numbers))
# res2 = list(map(lambda x:x**3,numbers))
# print(numbers)
# print(res)
# print(res2)

# line = list(map(int,input('Enter numbers :: ').split()))
# print(line)

# numbers = [4,5,8,7,4,1,2,5,6,9,3,2,5,4]
# res = list(filter(lambda x:x > 0 and x < 6,numbers))
# print(numbers)
# print(res)

# colors = ['RED', 'green', 'yellow', 'purple', 'lime',
#           'GOLD', 'white', 'black', 'tomato', 'magenta', 'cyan', 'blue']


# # def checkColor(color):
# #     return len(color) > 4


# print(colors)
# # new_colors = list(filter(checkColor, colors))
# # new_colors = list(filter(lambda color:len(color)>4, colors))
# # new_colors = list(filter(lambda color:color.find('bl') != -1, colors))
# new_colors = list(filter(lambda color:color.islower(), colors))
# print(new_colors)
