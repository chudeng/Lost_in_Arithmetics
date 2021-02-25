import random

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