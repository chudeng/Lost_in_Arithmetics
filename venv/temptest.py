infix = '3+1-2*2/2*(3+1*2/2-1)*3-2+1' # result = -15
answer = list(infix)

def intopost(answer):
    postfix = []
    stk = []
    for i in answer:
        if i.isdigit(): # 숫자면 postfix에 i 추가
             postfix.append(i)
             print(f'postfix에 {i} 숫자 추가')
        elif not i.isdigit():
            if i == '(':
                stk.append(i)   # '('면 stk에 i 추가
                print(f'elif not/if stk에 {i} 숫자 추가')
            elif i == '*' or i == '/':
                if len(stk) == 0 or stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '(':   # stk가 비어 있거나 stk[-1]이 '+' || '-' || '(' 면 stk에 i 추가
                    stk.append(i)
                    print(f'elif not/elif *,/ /if 조건 stk에 {i} 숫자 추가')
                else:
                    while len(stk) == 0 or stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '(':  # stk[-1]이 *||/ 면, stk[-1]를 postfix로 이동 후 stk에 i 추가
                        print('*, / while', stk)
                        postfix.append(stk.pop(-1))
                        print(stk)
                    stk.append(i)
                    print(f'elif not/elif *,/ /else 조건 stk에 {i} 숫자 추가')
            elif i == '+' or i == '-':
                if len(stk) == 0 or stk[-1] == '(':   # stk가 비어 있으면 stk에 i 추가
                    stk.append(i)
                    print(f'elif not/elif +,- /if 조건 stk에 {i} 숫자 추가')
                else:
                    while len(stk) == 0 or stk[-1] == '(':
                        print(stk[-1])
                        postfix.append(stk.pop(-1))
                        print(stk[-1])
                    stk.append(i)
                    print(f'elif not/elif +,- /else 조건 stk에 {i}{stk} 숫자 추가')
            elif i == ')':
                while stk:
                    if stk[-1] == '(':
                        stk.pop(-1)
                        break
                    else:
                        postfix.append(stk.pop(-1))
                        print(f'괄호 안의 {stk[-1]} postfix에 추가')
                        continue
    while stk:
        print(f'stk 안의 {stk[-1]} postfix에 추가')
        postfix.append(stk.pop(-1))
    print(postfix, len(postfix))
    return postfix

intopost(answer)