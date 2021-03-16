infix = '3+1-2*2/2*(3+1*2/2-1)*3-2+1' # result = -15
answer = list(infix)
print(answer)
while answer and (answer[-1] == '+'):
    answer.pop()
    print(answer)
print(answer)