from random import *

class game:
    def __init__(self, ID, score):
        self._ID = ID
        self._score = score
        print(self._ID, self._score)

    def stage(self, ID, score):
        pass

    def stage01(self, ID, score):
        # 문제(1~9 사이) 추출 및 출력
        print(f'여기까지 잘 왔어~{ID}, {score}')
        '''
        ST01_Q = []
        for i in (1, 10):
            ST01_Q.append(i+1)
        Question = random.choice(ST01_Q)
        print("Question: ", Question)

        # 숫자 선택지 추출
        ST01_NumsPieces = random.sample(ST01_Q, 5)

        # AllPieces에 모든 선택지 배열로 저장
        # 연산자및 숫자선택지 순으로 저장
        ST01_AllPieces = []
        for j in range(4):
            ST01_AllPieces.append(self.Operators[j])
        for i in range(5):
            ST01_AllPieces.append(ST01_NumsPieces[i])
        # 선택지 출력
        while True:
            for index, value in enumerate(ST01_AllPieces):
                print(index, value)
            userPick1 = ST01_AllPieces[int(input("Choose first piece for the answer: "))]
            print(userPick1)
            userPick2 = ST01_AllPieces[int(input("Choose second piece for the answer: "))]
            print(userPick2)
            userPick3 = ST01_AllPieces[int(input("Choose third piece for the answer: "))]
            print(userPick3)
            userAnswer = userPick1, userPick2, userPick3
            print(userAnswer)
            if userAnswer == Question:
                return(1)
                break
            elif (userPick1 or userPick2 or userPick3) == -1:
                pass
                '''



    def stage02(self):
        ST02_Q = randint(10, 99)
        print(ST02_Q)


    def stage03(self):
        ST03_Q = randint(100, 999)
        print(ST03_Q)


    def stage04(self):
        ST04_Q = randint(1000, 9999)
        print(ST04_Q)


    def stage05(self):
        ST05_Q = randint(1000, 9999)
        print(ST05_Q)


    def stage06(self):
        ST06_Q = randint(1000, 9999)
        print(ST06_Q)


    def stage07(self):
        ST07_Q = randint(1000, 9999)
        print(ST07_Q)


    def stage08(self):
        ST08_Q = randint(1000, 9999)
        print(ST08_Q)


    def stage09(self):
        ST09_Q = randint(1000, 9999)
        print(ST09_Q)


    def stage10(self):
        ST10_Q = randint(1000, 9999)
        print(ST10_Q)