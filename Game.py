import random

class game:
    def __init__(self, loadedID):
        self._loadedID = loadedID
        self._operators = ['+', '-', '*', '/']

    def stage(self):
        if self._loadedID[1][0] == 0:
            self.stage01()
        elif self._loadedID[1][0] == 1:
            self.stage02()
        elif self._loadedID[1][0] == 2:
            self.stage03()
        elif self._loadedID[1][0] == 3:
            self.stage04()
        elif self._loadedID[1][0] == 4:
            self.stage05()
        elif self._loadedID[1][0] == 5:
            self.stage06()
        elif self._loadedID[1][0] == 6:
            self.stage07()
        elif self._loadedID[1][0] == 7:
            self.stage08()
        elif self._loadedID[1][0] == 8:
            self.stage09()

    # infix 를 postfix로 변환
    def intopost(self, answer):
        postfix = []
        stk = []
        for i in answer:
            if i.isdigit():  # 숫자면 postfix에 i 추가
                postfix.append(i)
            else:  # 연산자이면...
                if i == '(':
                    stk.append(i)  # '('면 stk에 i 추가
                elif i == '*' or i == '/':
                    while True:
                        if stk[-1] == '*' or stk[-1] == '/':  # stk[-1]이 '*' || '/' stk[-1]을 postfix로 이동
                            postfix.append(stk.pop())
                            continue
                        else:
                            break
                    stk.append(i)
                elif i == '+' or i == '-':
                    while True:
                        if len(stk) == 0 or stk[-1] == '(':  # stk가 비어있거나 stk[-1]이 '(' 이면 stk에 i 추가
                            break
                        else:
                            postfix.append(stk.pop())  # stk[-1]을 postfix로 이동
                            continue
                    stk.append(i)
                elif i == ')':
                    while stk:
                        if stk[-1] == '(':
                            stk.pop(-1)
                            break
                        else:
                            postfix.append(stk.pop())
                            continue
        while stk:
            postfix.append(stk.pop(-1))
        return postfix

    # postfix를 받아 계산 후, 결과값 int로 변환 후 반환
    def operating(self, postfix):
        result = []
        for i in postfix:
            if i.isdigit():
                result.append(i)
            else:
                if i == '+':
                    sum = int(result[-2]) + int(result[-1])
                    result.pop()
                    result.pop()
                    result.append(sum)
                    print('else', result)
                elif i == '-':
                    sub = int(result[-2]) - int(result[-1])
                    result.pop()
                    result.pop()
                    result.append(sub)
                elif i == '*':
                    mul = int(result[-2]) * int(result[-1])
                    result.pop()
                    result.pop()
                    result.append(mul)
                elif i == '/':
                    dev = int(result[-2]) / int(result[-1])
                    result.pop()
                    result.pop()
                    result.append(dev)
        result = result[0]
        return result


    def stage01(self):
        # 문제(1~9 사이) 추출 및 출력
        ST01_list = []
        useranswer = 0
        for i in range(1, 10):
            ST01_list.append(i)
        Question = random.choice(ST01_list)

        # 숫자 선택지 추출
        ST01_NumsPieces = random.sample(ST01_list, 6)

        # AllPieces에 모든 선택지 배열로 저장
        # 연산자및 숫자선택지 순으로 저장
        ST01_AllPieces = ST01_NumsPieces + self._operators

        # 선택지 출력 및 답 입력
        # 선택지에서 3가지만 선택해서 식을 만들어야 함.
        while True:
            print("Question: ", Question)
            print('Options:',ST01_AllPieces)
            useranswer = input("Make arithmetic with 3 given options combination(Quit: -1): ")
            if useranswer == '-1':
                return useranswer
            elif len(useranswer) != 3:
                print('Must use 3 options.')
                continue
            else:
                postfix = self.intopost(useranswer)
                useranswer = self.operating(postfix)
                if useranswer == Question:
                    print('Correct!')
                    print(self._loadedID, type(self._loadedID))
                else:
                    print('Try again')
                    continue
        return useranswer


    def stage02(self):
        ST02_Q = random.randint(10, 99)
        print(ST02_Q)


    def stage03(self):
        ST03_Q = random.randint(100, 999)
        print(ST03_Q)


    def stage04(self):
        ST04_Q = random.randint(1000, 9999)
        print(ST04_Q)


    def stage05(self):
        ST05_Q = random.randint(1000, 9999)
        print(ST05_Q)


    def stage06(self):
        ST06_Q = random.randint(1000, 9999)
        print(ST06_Q)


    def stage07(self):
        ST07_Q = random.randint(1000, 9999)
        print(ST07_Q)


    def stage08(self):
        ST08_Q = random.randint(1000, 9999)
        print(ST08_Q)


    def stage09(self):
        ST09_Q = random.randint(1000, 9999)
        print(ST09_Q)


    def stage10(self):
        ST10_Q = random.randint(1000, 9999)
        print(ST10_Q)