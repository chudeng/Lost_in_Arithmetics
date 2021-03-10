infix = '3+1-2*2/2*(3+1*2/2-1)*3-2+1'
'''
3+1-2*2/2(3+1*2/2-1)*3-2+1
3+1-((((2*2)/2)(3+((1*2)/2)-1))*3)-2+1
31222*3122*/1+-/3*21+---+
'''
answer = list(infix)
postfix = []
stk = []


def intopost(answer):
    for i in range(len(answer)):
        if answer[i].isdigit():
            postfix.append(answer[i])
        elif not answer[i].isdigit():
            if answer[i] == '(':
                stk.append(answer[i])
            elif answer[i] == '*' or answer[i] == '/':
                if len(stk) == 0:
                    stk.append(answer[i])
                elif stk[-1] == '+' or stk[-1] == '-':
                    stk.append(answer[i])
                elif stk[-1] == '*' or stk[-1] == '/':
                    postfix.append(stk.pop(-1))
                    stk.append(answer[i])
            elif answer[i] == '+' or answer[i] == '-':
                if len(stk) == 0:
                    stk.append(answer[i])
                elif stk[-1] == '+' or stk[-1] == '-':
                    stk.append(answer[i])
                else:
                    stk.append(answer[i])
            elif answer[i] == ')':
                while stk:
                    if stk[-1] == '(':
                        stk.pop(-1)
                        break
                    else:
                        postfix.append(stk.pop(-1))
                        continue
    while stk:
        postfix.append(stk.pop(-1))
    print(postfix)
    return postfix


# postfix를 받아 계산 후, 결과값은 반환
def operating(postfix):
    result = []
    for i in postfix:
        if i.isdigit():
            result.append(i)
        else:
            if i == '+':
                stk = result.pop(-1) + result.pop(-1)
            elif i == '-':
                stk = result.pop(-1) - result.pop(-1)
            elif i == '*':
                stk = result.pop(-1) * result.pop(-1)
                print(stk)
            elif i == '/':
                stk = result.pop(-1) / result.pop(-1)
    print(int(result))

intopost(answer)
operating(postfix)


'''
from temptest import character_stat

instance = character_stat()
instance.set_all(100, 150)
instance.print()
'''


'''
inputID = 'asdfsd+f'
validID = 0
for i in inputID:
    print(i)
    print(type(i))
    validID = i.isalpha() or i.isdigit()
    if not validID == True:
        break
    else:
        continue


print(validID)
print(type(validID))
'''