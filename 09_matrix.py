
# # matrix = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9],
# #     ]

# # print(matrix)
# # for item in matrix:
# #     for li in item:
# #         print(li,end='\t')
# #     print()


# import random

# matrix = []
# row = 3
# col = 3
# # for i in range(row):
# #     numbers = []
# #     for j in range(col):
# #         numbers.append(random.randint(20,50))
# #     matrix.append(numbers)
# for i in range(row):
#     matrix.append([random.randint(20, 50) for i in range(col)])
# for i in matrix:
#     print(i)

# sum_ = 0
# for row in matrix:
#     sum_ += sum(row)
#     print('Res :: ', sum(row))
# print('Sum :: ', sum_)

# print()
# sum_ = 0
# row = 3
# for i in range(col):
#     sum_ = 0
#     for j in range(row):
#         sum_ += matrix[j][i]
#     print('Sum Column :: ', sum_)

# size = 3
# sum_main = 0
# sum_axi = 0
# for i in range(size):
#     sum_main += matrix[i][i]
#     sum_axi += matrix[i][size-1-i]# i{0} [size{3} - 1 - i{0}]{2} # i{1} [size{3} - 1 - i{1}]{1}  # i{2} [size{3} - 1 - i{2}]{0}
# print(sum_main)
# print(sum_axi)


import random
words = ['summer','winter','butterfly','programming']

word = random.choice(words)

print(word)

img = [
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .~G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .!G&&G7^^:::^^^:::::::^::~JG&@@@&G~.                
                                                .!G&&G~                  :?P&@@@&G~.                
                                                .!G@@G!.                 :?P&@@@&G~.                
                                                .^?YY?^                  :?P&@@@&G~.                
                                                  ....                   :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^7PPJ7!7YP5?:              :?P&@@@&G~.                
                                               .^!J555J7:.               :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^7PPJ7~7YP5?:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!YJ:                  :?P&@@@&G~.                
                                                  ..::.                  :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^?PPJ7~7YP5?:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                      .:^^....    ^75Y^                  :?P&@@@&G~.                
                                     .^75G5Y?!^:.:^75Y^                  :?P&@@@&G~.                
                                       .:~7JY555YJY5PY^                  :?P&@@@&G~.                
                                              .^~7YPGY^                  :?P&@@@&G~.                
                                                  ^75Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!YJ:                  :?P&@@@&G~.                
                                                  ..::.                  :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^?PPJ!~7YP5J:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                      .:^^....    ^75J^    ..::^:.       :?P&@@@&G~.                
                                     .^75G5Y?!^:.:^75Y~:^~!?YPGPJ~.      :?G&@@@&G~.                
                                       .:~7JY555JJJ5GG5Y555Y?!~:.        :?P&@@@&G~.                
                                              .^~7YGBP7^:.               :?P&@@@&G~.                
                                                  :!5Y^                  :?G&@@@&G~.                
                                                 .:!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!YJ:                  :?P&@@@&G~.                
                                                  ..::.                  :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^?PPJ!~7YP5J:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                      .:^^....    ^75J^    ..::^:.       :?P&@@@&G~.                
                                     .^75G5Y?!^:.:^75Y~:^~!?YPGPJ~.      :?G&@@@&G~.                
                                       .:~7JY555JJJ5GG5Y555Y?!~:.        :?P&@@@&G~.                
                                              .^~7YGBP7^:.               :?P&@@@&G~.                
                                                  :!5Y^                  :?G&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .!J5J^                  :?P&@@@&G~.                
                                               .~JPP7^.                  :?P&@@@&G~.                
                                             .!JGP7^.                    :?P&@@@&G~.                
                                           .!JGP7^.                      :?P&@@@&G~.                
                                         :!YGP!:.                        :?P&@@@&G~.                
                                       .!JP5!:                           :?P&@@@&G~.                
                                     .^755!:                             :?P&@@@&G~.                
                                      ::^:                               :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
    '''
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5B#&&&&&&&&&&&&&&&&&&&&&######B5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G!.                
                                                .!G&&G7^:::::::::::::::::~?P&@@@@G!.                
                                                .!G&&P~                  .75#@@@&G!.                
                                                 ~G@&G~                  .75&@@@@G!.                
                                               .!YB&#B5?^.               :75&@@@&G!.                
                                             .~?55?~~!J55?:              .75&@@@@G!.                
                                             :J5J!.   :!55!.             :75#@@@@G!.                
                                             :J5J!.   .!55!.             .75&@@@@G!.                
                                             .^7PPJ7!75P57:              .75&@@@@G!.                
                                               .^7YGBGJ!:                .75&@@@&G!.                
                                      .:^^:...   .^7YJ:    ..:^^:.       :75&@@@@G!.                
                                     .^75GP5J7~^::^75Y~:~!7JYPGPJ~.      :75#@@@@G!.                
                                        .^!?Y5PP55Y5GBPPPP5Y7!^:.        :75&@@@@G!.                
                                              :^!?5GBP?~:.               .75#@@@@G!.                
                                                  ^7YJ:                  :75&@@@@G!.                
                                                 .^7YJ^                  .75#@@@@G!.                
                                                 .^7YJ^                  .75&@@@@G!.                
                                                 .^7YJ^                  .75&@@@@G!.                
                                                 .^7YJ:                  .75&@@@@G!.                
                                                 .:!YJ:                  .75&@@@@G!.                
                                                 .!JG5^                  .75&@@@@G!.                
                                               .~?PGGP5?:                .75&@@@@G!.                
                                             .~?PP7^:~YP5?^              .75&@@@@G!.                
                                           .~JGP7^.   .~YP5J^            :75#@@@@G!.                
                                         .!JGP7:.        ^JPPJ^.         .75&@@@@G!.                
                                       :!YP5!:.            ^J5PJ~.       .75#@@@@G!.                
                                     .^?P5!:                 ^J5Y?:      .75#@@@@G!.                
                                      .::.                     .^^.      :75#@@@@G!.                
                                                                         :75&@@@&G!.                
                                                                         .75&@@@&G!.                
                                            ...........................  :7P&@@@@G!:..........      
                                           :7YYYYYYYYYYYYYYYYYYYYYYYYYYYY5GB&@@@@#P5YYYYYYYYJ7:     
                                           ~P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P~     
                                           ~P#&@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@&&&&&@&&@&&@@&#5^     
                                           .^!!77!!!!!!!!!!!!!!!!!!!!77!!!!!!77777!!77!!!!77!~.     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''',
]

answer = ['_' for i in word]
counter = len(word)
wrong = 0
answer[0] = word[0]
answer[-1] = word[-1]
while counter != 0 and wrong != 6:
    print(img[wrong])
    print(' '.join(answer))
    s = input("Enter letter > ")
    if len(s) != 1:
        print('Error')
        wrong += 1
        continue
    index = word.find(s)
    if index == -1:
        wrong+=1
    if index != -1 and answer[index] != '_':
        wrong+=1
    while index != -1:
        counter-=1
        answer[index] = s
        index = word.find(s,index+1)

if wrong == 6:
    print('Game Over')
    print(img[wrong])
else:
    print('Congratulation!!!! You Won!!!!')
