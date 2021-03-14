infix = '3+1-2*2/2*(3+1*2/2-1)*3-2+1' # result = -15
'''
3+1-2*2/2(3+1*2/2-1)*3-2+1
3+1-((((2*2)/2)(3+((1*2)/2)-1))*3)-2+1
31222*3122*/1+-/3*21+---+
'''
answer = list(infix)

def intopost(answer):
    postfix = []
    stk = []
    for i in answer:
        if i.isdigit(): # 숫자면 postfix에 i 추가
             postfix.append(i)
        elif not i.isdigit():
            if i == '(':
                stk.append(i)   # '('면 stk에 i 추가
            elif i == '*' or i == '/':
                if len(stk) == 0 or stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '(':   # stk가 비어 있거나 stk[-1]이 '+' || '-' || '(' 면 stk에 i 추가
                    stk.append(i)
                else:
                    while len(stk) == 0 or stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '(':  # stk[-1]이 *||/ 면, stk[-1]를 postfix로 이동 후 stk에 i 추가
                        postfix.append(stk.pop(-1))
                    stk.append(i)
            elif i == '+' or i == '-':
                if len(stk) == 0 or stk[-1] == '(':   # stk가 비어 있으면 stk에 i 추가
                    stk.append(i)
                else:
                    while len(stk) == 0 or stk[-1] == '(':
                        postfix.append(stk.pop(-1))
                    stk.append(i)
            elif i == ')':
                while stk:
                    if stk[-1] == '(':
                        stk.pop(-1)
                        break
                    else:
                        postfix.append(stk.pop(-1))
                        continue
    while stk:
        postfix.append(stk.pop(-1))
    print(postfix, len(postfix))
    postfix_demo_str = '31+22*2/312*2/+1-*3*-2-1+'
    postfix_demo = list(postfix_demo_str)
    return postfix_demo


# postfix를 받아 계산 후, 결과값은 반환
def operating(postfix):
    result = []
    for i in postfix:
        if i.isdigit():
            result.append(int(i))
            print(f'digit {i} added')
        else:
            if i == '+':
                print(f'sum {result[-1]} + {result[-2]} = {result[-1] + result[-2]} added')
                sum = result.pop(-1) + result.pop(-1)
                result.append(sum)
            elif i == '-':
                print(f'sub {result[-1]} - {result[-2]} = {result[-1] - result[-2]} added')
                sub = result.pop(-1) - result.pop(-1)
                result.append(sub)
            elif i == '*':
                print(f'mul {result[-1]} x {result[-2]} = {result[-1] * result[-2]} added')
                mul = result.pop(-1) * result.pop(-1)
                result.append(mul)
            elif i == '/':
                print(f'dev {result[-1]} / {result[-2]} = {result[-1] / result[-2]} added')
                dev = result.pop(-1) / result.pop(-1)
                result.append(dev)
    print('result', result, type(result))

postfix = intopost(answer)
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