import random
import time
from UserData import UserData as UD
from score import scoreCalc

class game:

    userData = UD()

    def __init__(self, loadedID):
        self._loadedID = loadedID
        self._operators = ['+', '-', '*', '/']
        self._userAnswer = ''

    def stage(self):
        if self._loadedID[1][0] == 1:
            self.stage01()
        elif self._loadedID[1][0] == 2:
            self.stage02()
        elif self._loadedID[1][0] == 3:
            self.stage03()
        elif self._loadedID[1][0] == 4:
            self.stage04()
        elif self._loadedID[1][0] == 5:
            self.stage05()
        elif self._loadedID[1][0] == 6:
            self.stage06()
        elif self._loadedID[1][0] == 7:
            self.stage07()
        elif self._loadedID[1][0] == 8:
            self.stage08()
        elif self._loadedID[1][0] == 9:
            self.stage09()
        return self._userAnswer


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
                        if len(stk) == 0:
                            stk.append(i)
                            break
                        elif stk[-1] == '*' or stk[-1] == '/':  # stk[-1]이 '*' || '/' stk[-1]을 postfix로 이동
                            postfix.append(stk.pop())
                            continue
                        else:
                            stk.append(i)
                            break
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
        print('======== Level 1 ========')
        ST01_list = []  # stage01에서 사용될 숫자 리스트
        useranswer = 0  # 입력받은 답을 저장 할 변수
        answerTime = 0  # 문제 푸는데 걸린 시간을 저장 할 변수
        tryTime = 1     # 문제 푸는 시도 횟수를 저장 할 변수
        userDic = self.userData.userLoad()
        print(userDic)
        # 문제(1~9 사이) 추출 및 출력
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
            print('Options:', ST01_AllPieces)
            timeBegins = time.time()
            self._userAnswer = input("Make arithmetic with 3 given options combination(Quit: -1): ")
            usedOptionCheck = 0 # 주어진 옵션만을 사용하여 식을 만들었는지 판단용 변수
            # 답변에 주어진 옵션 외에 조건이 포함 되어 있으면 usedOptionCheck 에 1을 저장. 아니면 0을 저장. -1이 입력 되었으면 초기화면
            for i in self._userAnswer:
                if self._userAnswer == '-1':
                    return self._userAnswer
                elif not i in str(ST01_AllPieces):
                    usedOptionCheck = 1
                    break
                else:
                    usedOptionCheck = 0
                    continue
            # 옵션에 없는 조건 사용 되었으면 continue, 아니면 pass
            if usedOptionCheck == 1:
                print('Ungiven options used.')
                continue
            else:
                pass
            # 3개 옵션 선택이 지켜지지 않았으면 continue. 그 외에는 답변 계산하여 맞으면 score 함수 호출, 틀렸으면 continue
            if len(self._userAnswer) != 3:
                print('Must use 3 options.')
                continue
            else:
                postfix = self.intopost(self._userAnswer)
                self._userAnswer = self.operating(postfix)
                if self._userAnswer == Question:
                    print('Correct!')
                    timeEnds = time.time()
                    answerTime = round(timeEnds - timeBegins, 2)
                    self._loadedID = scoreCalc.score(self, tryTime, answerTime)
                    userDic[self._loadedID[0]] = self._loadedID[1]
                    self.userData.userWrite(userDic)
                    return self._userAnswer
                else:
                    print('Try again')
                    tryTime += 1
                    continue
        return useranswer


    def stage02(self):
        print('======== Level 2 ========')
        ST02_list = []  # stage01에서 사용될 숫자 리스트
        useranswer = 0  # 입력받은 답을 저장 할 변수
        answerTime = 0  # 문제 푸는데 걸린 시간을 저장 할 변수
        tryTime = 1  # 문제 푸는 시도 횟수를 저장 할 변수
        userDic = self.userData.userLoad()
        print(userDic)
        # 문제(1~9 사이) 추출 및 출력
        for i in range(1, 10):
            ST02_list.append(i)
        Question = random.choice(ST02_list)

        # 숫자 선택지 추출
        ST02_NumsPieces = random.sample(ST02_list, 6)

        # AllPieces에 모든 선택지 배열로 저장
        # 연산자및 숫자선택지 순으로 저장
        ST02_AllPieces = ST02_NumsPieces + self._operators

        # 선택지 출력 및 답 입력
        # 선택지에서 3가지만 선택해서 식을 만들어야 함.
        while True:
            print("Question: ", Question)
            print('Options:', ST02_AllPieces)
            timeBegins = time.time()
            self._userAnswer = input("Make arithmetic with 5 given options combination(Quit: -1): ")
            usedOptionCheck = 0  # 주어진 옵션만을 사용하여 식을 만들었는지 판단용 변수
            # 답변에 주어진 옵션 외에 조건이 포함 되어 있으면 usedOptionCheck 에 1을 저장. 아니면 0을 저장. -1이 입력 되었으면 초기화면
            for i in self._userAnswer:
                if self._userAnswer == '-1':
                    return self._userAnswer
                elif not i in str(ST02_AllPieces):
                    usedOptionCheck = 1
                    break
                else:
                    usedOptionCheck = 0
                    continue
            # 옵션에 없는 조건 사용 되었으면 continue, 아니면 pass
            if usedOptionCheck == 1:
                print('Ungiven options used.')
                continue
            else:
                pass
            # 3개 옵션 선택이 지켜지지 않았으면 continue. 그 외에는 답변 계산하여 맞으면 score 함수 호출, 틀렸으면 continue
            if len(self._userAnswer) != 5:
                print('Must use 3 options.')
                continue
            else:
                postfix = self.intopost(self._userAnswer)
                self._userAnswer = self.operating(postfix)
                if self._userAnswer == Question:
                    print('Correct!')
                    timeEnds = time.time()
                    answerTime = round(timeEnds - timeBegins, 2)
                    self._loadedID = scoreCalc.score(self, tryTime, answerTime)
                    userDic[self._loadedID[0]] = self._loadedID[1]
                    self.userData.userWrite(userDic)
                    return self._userAnswer
                else:
                    print('Try again')
                    tryTime += 1
                    continue
        return useranswer


    def stage03(self):
        print('3단계까지 왔음')
        pass

    def stage04(self):
        print('4단계까지 왔음')
        pass


    def stage05(self):
        print('5단계까지 왔음')
        pass


    def stage06(self):
        print('6단계까지 왔음')
        pass


    def stage07(self):
        print('7단계까지 왔음')
        pass


    def stage08(self):
        print('8단계까지 왔음')
        pass


    def stage09(self):
        print('9단계까지 왔음')
        pass


    def stage10(self):
        print('10단계까지 왔음')
        pass