
# num = None
# num2 = None

# while num == None or num2 == None or num2 == 0:
#     try:
#         num = int(input('Enter number > '))
#         num2 = int(input('Enter number > '))
#         print(num / num2, num3)
#     except ValueError:
#         print('Error Value')
#     except ZeroDivisionError:
#         print('division by zero')
#     except Exception:
#         print('Error')
# print('End!!!')

# try:
#     age = int(input('Enter age :: '))
#     if age < 0:
#         raise Exception('Age error. Age < 0')
#     if age > 126:
#         raise Exception('Age error. Age > 126')
# except Exception as ex:
#     print(ex, type(ex).__name__)
# else:
#     print('Good!!!!')
# finally:
#     print('Finally')


# colors = ['red','blue','green','yellow']
# try:
#     index = int(input('Enter position color :: '))
#     print(colors[index])
# except ValueError:
#     print('Value Error')
# except IndexError:
#     print('Index Error')
#     print(colors[-1])


# task 1
# Напишіть програму, яка дозволяє користувачеві обчислити частку (ділення одного числа на інше) двох чисел. Програма приймає два значення з клавіатури і повертає результат операції на екран. Обробіть виняток, що виникає під час ділення на нуль, і виведіть повідомлення про помилку.
# first = int(input('Enter first number :: '))
# second = int(input('Enter second number :: '))
# try:
#     print(first / second)
# except Exception:
#     print('На нуль ділити не можна!!!!!!')


# Завдання 2
# Реалізуйте перше завдання через функцію. Функція повинна приймати два параметри і відображати результат ділення на екран. Створіть дві версії реалізації функції:

# Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції.
# task 2(1)
# def divis(a,b):
#     if b == 0:
#         raise ZeroDivisionError
#     print(a/b)


# first = int(input('Enter first number :: '))
# second = int(input('Enter second number :: '))
# try:
#    divis(first,second)
# except ZeroDivisionError:
#     print('На нуль ділити не можна!!!!!!')

# task 2(1)
# def divis(a, b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print('На нуль ділити не можна!!!!!!')

# first = int(input('Enter first number :: '))
# second = int(input('Enter second number :: '))
# divis(first,second)


# Завдання 3
# Напишіть програму, яка приймає рядок і намагається перетворити його на число.

# Обробіть виняток, що виникає при неможливості перетворення, і виведіть повідомлення про помилку.

# Завдання 4
# Реалізуйте третє завдання через функцію. Функція повинна приймати рядок і відображати результат перетворення на екран. Створіть дві версії реалізації функції:

# Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції.

# number = input('Enter number :: ')
# try:
#     int(number)
# except ValueError:
#     print('Введіть тільки цифри')


# def convert(line):
#     int(line)

# number = input('Enter number :: ')
# try:
#     convert(number)
# except ValueError:
#     print('Введіть тільки цифри')

# def convert(line):
#     try:
#         int(line)
#     except ValueError:
#         print('Введіть тільки цифри')


# number = input('Enter number :: ')
# convert(number)

import math
print(math.sqrt(4))