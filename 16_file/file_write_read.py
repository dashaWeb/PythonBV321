# відркити файл
# читати файл
# записати у файл
# закрити файл

# url = r'C:\Users\dev\Desktop\PythonBV321\16_file\my.txt'
# file = open(url)
# # print(file.read())
# # print(file.readline().strip())
# # print(file.readlines())
# print(file.read(15))

# file.close()


# with open(url) as file:
#     line = file.read()
#     print(type(line))


# url_2 = r'16_file/write.txt'
# with open(url_2,'w') as file:
#     file.write('Lorem ipsum')


# url_2 = r'16_file/write.txt'
# with open(url_2,'a') as file:
#     file.write('Lorem ipsum\n')


# with open(url_2,'w') as file:
#     file.write('')

# lines = [
#     'Duis malesuada sem quis sapien lobortis facilisis.',
#     'Cras sit amet orci semper, porta sem sit amet, mattis leo.',
#     'Suspendisse aliquam dolor nec aliquam egestas.',
# ]
# url_2 = r'16_file/write.txt'

# with open(url_2,'w') as file:
#     # file.write(lines)
#     counter = 1
#     for line in lines:
#         file.write(f'{counter}. {line}\n')
#         counter+=1

# with open(url_2,'w') as file:
#     file.writelines(lines)

# with open(url_2,'w') as file:
    
#     file.write('\n'.join(lines))


# def readFile(fname):
#     with open(fname,'r') as file:
#         return file.read()

# def appFile(fname,info):
#     with open(fname,'a') as file:
#         file.write(info)

# url_write = '16_file/my.txt'
# url_read = '16_file/write.txt'

# text = readFile(url_read)
# appFile(url_write,text)

# lines = []
# with open('16_file/my.txt') as file:
#     lines = file.readlines()

# with open('16_file/new.txt','w') as file:
#     for line in lines[::-1]:
#         file.write(line.strip()+'\n')

# with open('16_file/my.txt','a') as file:
#     file.write(str(5))
# line = ''
# with open('16_file/my.txt',encoding='utf-8') as file:
#     line = file.read()

# def delPunct(line,mark):
#     new_str = ''
#     for li in line:
#         if li not in mark:
#             new_str+=li
#     return new_str
# symbol = r'''./\!?-—():,«»'"'''
# line = delPunct(line,symbol)
# line = line.split()
# with open('16_file/words.txt','w',encoding='utf-8') as file:
#     for item in line:
#         if len(item) >= 7:
#             file.write(item + '\n')
#     file.write('*'*12)       

# import requests

# img = requests.get('https://t3.ftcdn.net/jpg/02/46/14/48/360_F_246144813_VSYaSoJgpD90TY566bpXRLTPCIjnD1SY.jpg')
# with open('16_file/img.jpg','wb') as file:
#     file.write(img.content)

