# 5! --> 5 * 4!
# 4! --> 4 * 3!
# 3! --> 3 * 2!
# 2! --> 2 * 1!
# 1! = 1
# 0! = 1


# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))

# def power(n,ex):
#     if ex == 1:
#         return n
#     if ex == 0:
#         return 1
#     return n * power(n,ex-1)
# print(power(12,2))

# def show(number):
#     if number == 0:
#         return
#     print('*',end='')
#     show(number-1)
#     print('-',end='')

# show(10)


# def showRange(a, b):
#     print(a, end=' ')
#     if a == b:
#         return
#     showRange(a+1, b)

# def showRange2(a, b):
#     print(b, end=' ')
#     if a == b:
#         return
#     showRange2(a, b-1)

# showRange(1, 10)
# print()
# showRange2(1, 10)


# def pal(number):
#     if number == 0:
#         return
#     print(number%10,end='')
#     pal(number//10)
# pal(12345)

def sumNum(number):
    if number < 10:
        return number
    return number% 10 + sumNum(number//10)
print(sumNum(123456))