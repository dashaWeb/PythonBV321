# ==, !=, <, >, <=, >=  ---- True, False

# a = 2
# b = 2
# print(a, "==", b, "--->", a == b)  # False
# print(a, "!=", b, "--->", a != b)  # True
# print(a, "> ", b, "--->", a > b)  # False
# print(a, "< ", b, "--->", a < b)  # True
# print(a, "<=", b, "--->", a <= b)  # True
# print(a, ">=", b, "--->", a >= b)  # False

# and, or

# age = int(input("Enter age :: "))
# # if age >= 18 and age <= 126:
# if  18 <= age <= 126:
#     print("ok")
# else:
#     print("Error")


# day = int(input("Enter number day [1-7] :: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Error")

# login = input("Enter login :: ")
# if login == "admin" or login == "Admin":
#     password = input("Enter password :: ")
#     if password == "step":
#         print("Welcome")
#     else:
#         print("Error password")
# elif login == "exit":
#     print("Goodbye")
# else:
#     print("Error login")


# day = int(input("Enter number day [1-7] :: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Error")


# day = int(input("Enter number day [1-7] :: "))

# match day: # day == 3
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Error")


day = 31
month = 12
year = 2004
print("{}.{}.{}".format(day, month, year))
day += 1
fullDays = 0

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    fullDays = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    fullDays = 30
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        fullDays = 29
    else:
        fullDays = 28

if day > fullDays:
    day = 1
    month += 1

if month > 12:
    month = 1
    year += 1

print("{}.{}.{}".format(day, month, year))
