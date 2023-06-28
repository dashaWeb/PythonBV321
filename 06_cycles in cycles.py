
# Task 1
# n = 10
# n2 = 15
# for j in range(n, n2+1):
#     i = 0
#     print(j, " --> ", sep="", end="")
#     while i < j:
#         i += 1
#         if j % i == 0:
#             print(i, " ", end="")
#     print()


# Task 3
# Створити програму, яка виводить на екран прості числа в
# діапазоні від 2 до 1000. (Число називається простим, якщо воно
# ділиться тільки на 1 і на саме себе без залишку; причому числа 1
# і 2 за прості не вважаються).

# start = 2
# end = 1000
# for j in range(start+1,end+1):
#     i = 2
#     while i < j:
#         if j % i == 0:
#             break
#         i += 1
#     else:
#         print(j, "\t", end="")
# print()

# Task 3
# 3. На валізі стоїть тризначний код. Він складається з цифр, які не
# повторюються. Напишіть програму, яка виведе всі можливі такі
# комбінації цифр. А також визначте, скільки часу знадобиться для
# відкриття валізи, в гіршому випадку, якщо на один такий набір
# витрачається 3 секунди.
# time = 0
# for i in range(10):  # генерація першої цифри
#     for j in range(10):  # генерація другої цифри
#         for q in range(10):  # генерація третьої цифри
#             if i != j and j != q and q != i:  # перевірка, щоб всі цифри були різні
#                 print(i, j, q, sep="")
#                 time += 1
# time *= 3
# print(time//60, ":", time % 60, sep="")


# 4. Наприкінці травня фірма формує звіт по заробітній платі 12
# співробітників за весняний квартал. Написати програму, яка
# запитуватиме суму заробітної плати кожного співробітника за
# Березень, Квітень і Травень. Необхідно визначити:
# ■ виплату по кожному співробітнику за квартал;
# ■ загальну виплату по всім співробітникам за квартал.


# Task 5
# Вивести на дисплей календар на обраний місяць з
# урахуванням зазначеного номера дня тижня для початку місяця.
# Підказка. Програму умовно розбити на дві частини. Перший цикл
# виводитиме потрібну кількість порожніх клітин. Другий же цикл
# почне виводити календар з першого дня до останнього дня в
# заданому місяці. Перехід на новий рядок вважати кратним семи із
# зазначеним зсувом номера дня тижня.
# Бонусне завдання: визначити кількість вихідних у заданому
# місяці.
# Приклад виконання програми:

# month = int(input("Enter month [1,12] ---  "))
# day = int(input("Enter start day [1 - 7] --- "))
# counter = 0
# days = 0
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days = 30
# elif month == 2:
#     year = int(input("Enter year"))
#     if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
#         days = 29
#     else:
#         days = 28
# else:
#     print("Error")
# day -= 1
# for i in range(1, days+1):
#     if i == 1:
#         print('\t'*day, end="")
#     print(i, "\t", end="")
#     if (day + i) % 7 == 0:
#         print()
#         counter += 1
#         if i != 1:
#             counter += 1
# print()
# print("Result :: ", counter)


# task 6

# number = 15
# start_space = 0
# space = number // 2 - 1
# flag = True
# i = 0
# while i < number-1:
#     i += 1
#     print(' '*start_space, '*', ' '*space, '*', ' '*space, '*', sep="")
#     if i == number // 2:
#         print('*'*number)
#         flag = False
#         continue
#     if flag:
#         start_space += 1
#         space -= 1
#     else:
#         start_space -= 1
#         space += 1


# task 4
totalSum = 0
sum = 0
for i in range(3):
    sum = 0
    for j in range(3):
        sum += int(input("Enter sum : "))
    print("Sum :: ", sum)
    totalSum += sum
print("Total sum :: ", totalSum)
