

# fruit = ['banana','orange','plum',True,458]
# colors = list(('red','green','blue','yellow'))
# print(len(fruit)) #довжина списка(кількість елементів)
# # print(colors[-1::-1])

# for item in colors:
#     # print(item, ' ::: ', len(item))
#     # print(item.upper())
#     for s in item:
#         print(s,end=" - ")
#     print()

# number = [i for i in range(1,11)]
# import random

# number = [random.randint(20,50)  for i in range(10)]
# print(number)
# # line = [s for s in 'language'[2:6]]
# line = [s for s in 'language']
# print(line)
# print(' '.join(line))
# for i in range(len(number)):
#     number[i] = str(number[i])
# print(number)
# print(' '.join(number))

# line = 'blue green yellow orange blue'
# list_colors = line.split(' ')
# print(list_colors)
# list_colors.append('purple')  # додає новий елемент в кінець списку
# print(list_colors)

# # додає новий елемент в список за вказаною позицією
# list_colors.insert(2, 'magenta')
# print(list_colors)

# list_colors.extend(['pink', 'cyan', 'lime'])
# print(list_colors)

# list_colors.remove('blue')  # видаляє елемент списку за значенням
# print(list_colors)

# list_colors.pop(5)  # видаляє елемент списку за позицією
# print(list_colors)

# list_colors.pop()
# print(list_colors)

# # list_colors.clear() #видаляє всі елементи списку
# # print(list_colors)

# print("Index ", list_colors.index('blue'))
# print("Count", list_colors.count('blue'))

# list_colors.sort()
# print(list_colors)

# list_colors.sort(reverse=True)
# print(list_colors)
# import random
# numbers = [random.randint(10,100) for i in range(10)]

# print("Print list :: ",numbers)
# print("Max :: ",max(numbers))
# print("Min :: ",min(numbers))
# print("Sum :: ",sum(numbers))
# print("Sort :: ",sorted(numbers,reverse=True))

# colors = 'blue green yellow orange blue'.split(' ')

# # clone = colors.copy()
# # # clone = list(colors)
# # clone = colors[:]

# print('Colors::',colors)
# print('Clone',clone)

# clone[0] = 'red'
# print('\nColors::',colors)
# print('Clone',clone)
# print(colors is clone)


# numbers = []
# count = int(input('Enter count '))

# for i in range(count):
#     numbers.append(int(input('Enter number ')))

# numb = int(input('Enter ind number '))
# print(numbers.count(numb))

# numbers = input('Enter number of space ').split(' ')
# numb = input('Enter ind number ')
# print(numbers.count(numb))


# numbers = input('Enter number of space ').split(' ')
# numbers = [int(item) for item in numbers]
# print(sum(numbers))
# print(sum(numbers)/len(numbers))

# 24+35
# reg = input('Example [21+2] > ')

# if reg.find('+') != -1:
#     numbers = reg.split('+')
#     numbers = [int(number) for number in numbers]
#     print(f'Result :: {numbers[0]+numbers[1]}')

# import random
# minus = 0
# plus = 0
# zero = 0

# numbers = [random.randint(-10,10) for i in range(10)]
# min = min(numbers)
# max = max(numbers)

# print(numbers)

# for number in numbers:
#     if number > 0:
#         plus+=1
#     elif number < 0:
#         minus+=1
#     elif number == 0:
#         zero+=1
# print('Max --> ',max)
# print('min --> ',min)
# print('minus --> ',minus)
# print('plus --> ',plus)
# print('zero --> ',zero)