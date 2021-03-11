infix = '3+1-2*2/2*(3+1*2/2-1)*3-2+1'
infix_list = list(infix)
while infix_list:
    print(infix_list[-1])
    infix_list.pop(-1)
    print(infix_list)