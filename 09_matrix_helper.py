
# import random
# list_ = [random.randrange(1,10) for i in range(10)]
# max_ = max(list_)
# min_ = min(list_)

# index_min = 0
# index_max = 0

# index_min = list_.index(min_)
# index_max = list_.index(max_)

# print(list_)
# print('min ',index_min)
# print('max ',index_max)

# start,end = 0,0

# if index_min < index_max:
#     start = index_min
#     end = index_max
# else:
#     start = index_max
#     end = index_min
# for i in range(start + 1,end):
#     list_[i]*=2 # list_[i] = list_[i] * 2

# print(list_)



#[1,2,3,4,5,6,7,8,9,10]
#[0] [0+1]
#[2] [2+1]
#[4] [4+1]

# import random
# list_ = [random.randrange(1,10) for i in range(10)]

# for i in range(len(list_))[::2]:
#     tmp = list_[i]
#     list_[i] = list_[i+1]
#     list_[i+1] = tmp
# print(list_)

# import random
# list_ = [random.randrange(1,10) for i in range(10)]
# print(list_)
# for i in range(len(list_)):
#     for j in range(i+1,len(list_)):
#         if list_[i] == list_[j]:
#             print(list_[i])
#             break

import random
row = 3
col = 4
matrix = [[random.randrange(1,10) for i in range(col)] for j in range(row)]

for item in matrix:
    for li in item:
        print(li,'\t',end='')
    print('| ',sum(item))
print('-'*(8 * (col + 1)))
totalSum = 0
for i in range(col):
    sum = 0
    for j in range(row):
        sum+= matrix[j][i]
    print(sum,'\t',end='')
    totalSum+=sum
print('| ',totalSum)  