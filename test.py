# 유저 데이터를 딕셔너리로 저장하는 함수 테스트
userDic = {'chudeng':[1,2,3], 'chudang':[4,5,6]}
while True:
    inputID = input('input your ID: ')
    user = inputID in userDic
    print(user)
    print(type(userDic))
    if user == True :
        print('used')
        print(userDic)
        continue
    else:
        userDic.setdefault(inputID)
        print('Can use it')
        print(userDic)
        break
print(userDic.keys())
with open("test.dat", "w") as w:
    print(userDic, file=w)

with open("test.dat", "r") as r:
    # eval을 통해 파일을 읽어올때 'dict' type으로 읽어옴
    userDic = eval(r.read())
    print(type(userDic))
    print(userDic)

for index, (keys, values) in enumerate(userDic.items()):
    print(index+1,keys,values)


'''
for userID in userDic.keys():
    if userID == inputID:
        print("ID already used.")
        break
    else:
        pass


print("ID stored.")
userDic.setdefault(inputID)
score = []
for num in range(3):
    score.append(num)
    num += 1
userDic.update(num = score)
print(userDic)
'''

#for line, column in userDic.items():
'''
    for listIndex in column:
        print(listIndex, end=' ')

    for index in userDic:
        print(userDic['Empty'][index])

with open('userdata.dat', 'w') as UDW:
    for line in userList:
        for column in userList[line]:
            userdata = userList[line][column]
            UDW.write(userdata, '\t')
        UDW.write('\n')
        
with open('userdata.dat', 'r') as UDR:
    UDR.read

ST01_Q = []
for i in range(9):
    ST01_Q.append(i+1)

Question = random.choice(ST01_Q)
print("Question: ", Question)

# 숫자 선택지 추출
ST01_NumsPieces = random.sample(ST01_Q, 5)
Operators = ['+', '-', '*', '/']
# AllPieces에 모든 선택지 배열로 저장
# 연산자및 숫자선택지 순으로 저장
ST01_AllPieces = []
for j in range(4):
    ST01_AllPieces.append(Operators[j])
for i in range(5):
    ST01_AllPieces.append(ST01_NumsPieces[i])
# 선택지 출력
for index, value in enumerate(ST01_AllPieces):
    print(f'{index+1}: {value}')
userPick1 = ST01_AllPieces[int(input("Choose first piece for the answer: ")) - 1]
print(userPick1)
userPick2 = ST01_AllPieces[int(input("Choose second piece for the answer: ")) - 1]
print(userPick2)
userPick3 = ST01_AllPieces[int(input("Choose third piece for the answer: ")) - 1]
print(userPick3)
userAnswer = userPick1, userPick2, userPick3
print(userAnswer)
'''

