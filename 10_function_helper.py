# task 5
# 1, 10
# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
# 10, 1
# 1 , 10

# way 1
# def multRange(start,end):
#     if start > end:
#         start,end = end,start
#     mult = 1
#     for i in range(start,end+1):
#         mult *= i
#     return mult
# print(multRange(10,5))

# way 2
# def getRangList(start,end):
#     if start > end:
#         start,end = end,start
#     tmp = [i for i in range(start,end+1)]
#     return tmp

# def multRange(start,end):
#     mult = 1
#     for item in getRangList(start,end):
#         mult*=item
#     return mult
# print(multRange(1,10))

# #task 6
# def numberOfDigits(number):
#     counter = 0
#     while number != 0:
#         number //= 10
#         counter += 1
#     return counter
# print(numberOfDigits(1452))

# #task 7
# def checkPalindrom(number):
#     return str(number) == str(number)[-1::-1]

# print(checkPalindrom(12321))
