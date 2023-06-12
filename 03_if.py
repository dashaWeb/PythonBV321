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

login = input("Enter login :: ")
if login == "admin" or login == "Admin":
    password = input("Enter password :: ")
    if password == "step":
        print("Welcome")
    else:
        print("Error password")
elif login == "exit":
    print("Goodbye")
else:
    print("Error login")