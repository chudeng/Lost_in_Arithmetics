# 실제 게임을 수행 함.
# Main.py로 부터 넘겨받은 유저 정보를 토대로 수행.
# stage01 ~ stage10 까지 있으나, 03부턴 미 구현


import random                       # 문제와 선택지생성을 위한 라이브러리
import time                         # 문제풀이 시간기록을 위한 라이브러리
from UserData import UserData as UD # userdata.dat file 관리 라이브러리
from score import scoreCalc         # 문제풀이 후 점수 계산을 위한 라이브러리

class game:
    # UD library instance 할당
    userData = UD()

    # main.py 에서 load된 user ID 정보 할당.
    def __init__(self, loadedID):
        self._loadedID = loadedID
        self._operators = ['+', '-', '*', '/']
        self._userAnswer = ''

    # load된 user ID의 level 맞는 게임 호출
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


    # 유저가 입력한 infix 를 postfix로 변환. 유저가 입력한 식을 받음.
    def intopost(self, answer):
        # postfix: 후위표기식 저장을 위한 배열. stk: 후위표기식 변환을 위한 연산자 저장 배열
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
                        if len(stk) == 0:   # stk가 비어 있으면 stk에 i 추가
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
                        if len(stk) == 0 or stk[-1] == '(':  # stk가 비어있거나 stk[-1]이 '(' 이면 break
                            break
                        else:
                            postfix.append(stk.pop())  # stk[-1]을 postfix로 이동
                            continue
                    # while 문 종료 후 stk에 i 추가
                    stk.append(i)
                elif i == ')': # ')'을 만나면 stk의 원소를 pop하여 '(' 만날때까지 postfix에 추가. '('를 만나면 '('삭제 후 break
                    while stk:
                        if stk[-1] == '(':
                            stk.pop(-1)
                            break
                        else:
                            postfix.append(stk.pop())
                            continue
        while stk:  # 남은 stk의 원소가 비워질때까지 pop하여 postfix에 추가
            postfix.append(stk.pop(-1))
        return postfix

    # postfix를 받아 계산 후, 결과값 int로 변환 후 반환
    def operating(self, postfix):
        # 결과값을 저장할 변수
        result = []
        # postfix 검토
        for i in postfix:
            # 숫자면 result에 추가
            if i.isdigit():
                result.append(i)
            # 연산자면 result[-2]와 result[-1]의 값을 연산 후 결과값 result에 추가.
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

    # stageXX: stage에서 load된 ID의 level에 따라 호출될 게임 01 ~ 10까지.
    # stage03부터는 미구현
    def stage01(self):
        print('======== Level 1 ========')
        ST01_list = []  # stage01에서 사용될 숫자 리스트
        useranswer = 0  # 입력받은 답을 저장 할 변수
        answerTime = 0  # 문제 푸는데 걸린 시간을 저장 할 변수
        tryTime = 1     # 문제 푸는 시도 횟수를 저장 할 변수
        userDic = self.userData.userLoad()  # 플레이 유저의 정보
        print(userDic)
        # 문제 및 선택지 뽑기를 위한 숫자 list
        for i in range(1, 10):
            ST01_list.append(i)
        Question = random.choice(ST01_list) # 숫자 리스트에서 랜덤으로 문제 선택

        # 숫자 선택지 추출(6개)
        ST01_NumsPieces = random.sample(ST01_list, 6)

        # AllPieces에 모든 선택지 배열로 저장
        # 연산자및 숫자선택지 순으로 저장
        ST01_AllPieces = ST01_NumsPieces + self._operators

        # 선택지 출력 및 답 입력
        # 선택지에서 3가지만 선택해서 식을 만들어야 함.
        while True:
            print("Question: ", Question)
            print('Options:', ST01_AllPieces)
            timeBegins = time.time() # 문제풀이 경과시간 타임어택 start
            self._userAnswer = input("Make arithmetic with 3 given options combination(Quit: -1): ") # 사용자 입력 답
            usedOptionCheck = 0 # 주어진 옵션만을 사용하여 식을 만들었는지 판단용 변수
            # 주어진 선택지(ST01_AllPieces) 외의 조건이 답변에 포함 되어 있으면 usedOptionCheck 에 1을 저장. 아니면 0을 저장. -1이 입력 되었으면 초기화면
            for i in self._userAnswer:
                if self._userAnswer == '-1':
                    return self._userAnswer
                elif not i in str(ST01_AllPieces):
                    usedOptionCheck = 1
                    break
                else:
                    usedOptionCheck = 0
                    continue
            # 선택지에(ST01_AllPieces) 없는 조건 사용 되었으면 다시 입력, 아니면 pass
            if usedOptionCheck == 1:
                print('Ungiven options used.')
                continue
            else:
                pass
            # 3개 옵션 선택이 지켜지지 않았거나 오답이면 다시 입력. 그 외에는 답변 계산하여 맞으면 score 함수 호출.
            if len(self._userAnswer) != 3:
                print('Must use 3 options.')
                continue
            else:
                postfix = self.intopost(self._userAnswer)   # 답변 postfix로 변환
                self._userAnswer = self.operating(postfix)  # postfix 계산값을 self._userAnswer에 반환
                # 정답이면 점수계산
                if self._userAnswer == Question:
                    print('Correct!')
                    timeEnds = time.time()  # 문제풀이 경과시간 타임어택 stop
                    answerTime = round(timeEnds - timeBegins, 2) # 경과시간 계산(소수점 2자리까지)
                    self._loadedID = scoreCalc.score(self, tryTime, answerTime) # 경과시간, 시도 횟수를 반영하여 점수계산
                    userDic[self._loadedID[0]] = self._loadedID[1] # 계산된 점수 반영
                    self.userData.userWrite(userDic) # userdata.dat에 변경된 정보 업데이트
                    return self._userAnswer
                # 오답이면 다시 입력 및 시도 횟수 증가.
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