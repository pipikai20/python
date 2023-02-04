max_level=10
for current_level in range(1,max_level+1):
    for i in range(max_level-current_level):
        print(' ',end='') #在一行中连续打印多个空格
    for j in range(2*current_level-1):
     print('*',end='') #在一行中连续打印多个空格
    print()