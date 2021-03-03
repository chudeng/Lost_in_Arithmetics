from UserData import UserData as UD

class userInforSet:

    def __init__(self, userDic, Level, Score):
        self.userDic = userDic
        self.Level = Level
        self.Score = Score


    # 초기 로그인 화면
    # 유저리스트와 선택 옵션
    def userLogin(self):
        for i in range(10):
            print(f"{i+1} ':' self.userList[i]\n")
        print("1. New Game\n2. Load Game\n3. User Manager\n")
        while True:
            select = int(input("Select number:"))
            if select == 1 or 2 or 3:
                return (select)
            else:
                continue


    # 새로운 사용자 생성 매서드
    def userCreation(self):
        # userdata.dat 내용을 dict type으로 load
        self.userDic = UD.userLoad()
        # 새롭게 생성할 ID type(1자 이상 8자 이하)
        inputID = input('Please input ID(Max 8 letters): ')
        while True:
            if len(inputID) > 8:
                inputID = input("Please input ID(Max 8 letters)")
                continue
            elif len(inputID) <= 0:
                inputID = input("Please input ID(Max 8 letters)")
                continue
            else:
                # 생성요청 ID가 겹치는게 있으면(if true) 다시 입력, 없으면(else) userDic에 key(생성 ID)와 value([0, 0]배열) 추
                emptyID = inputID in self.userDic
                if emptyID == True:
                    print("The ID already used.")
                    continue
                else:
                    # 생성요청한 ID 최종 확인
                    # 'if ture'이면 self.userDic에 추가 후 UD.userWrite()로 userdata.dat file 에 업데이트
                    while True:
                        confirmation = input(f"{inputID} confirm?(y/n)")
                        if confirmation == "y" or "Y":
                            self.userDic.setdefault(inputID, [0,0])
                            UD.userWrite(self.userDic)
                            break
                        elif confirmation == "n" or "N":
                            self.userCreation()
                            break


    # 사용자 정보 확인
    # 기존 사용자이면, 해당 정보 로드
    # 새로운 사용자이면, 사용자생성(userCreation) 매서드 호출
    def userSelection(self):
        self.userDic = UD.userLoad()
        while True:
            for index, (key, value) in enumerate(self.userDic.items()):
                print(f"ID: {key}, Level & Score: {value}\n")
                keyList = list(self.userDic.keys())
                inputID = input("Please input ID(Back[-1], ID manage[0]): ")
                if inputID == -1:
                    self.userLogin()
                elif self.ID == 0:
                    self.userListManage()
                else:
                    for i in keyList:
                        if i == self.ID:
                            return (self.ID, self.userDic.get(self.ID))
                        else:
                            print("Please input right ID")
                            continue


    #사용자 정보 관리(확인 및 삭제)
    def userListManage(self):
        self.userDic = UD.userLoad()
        for index, (key, value) in enumerate(self.userDic()):
            print(f"ID: {key}, Level&Score: {value}\n")
        self.ID = input("Please input ID to be deleted(Quit: 0):"))
        if userNumber > 10:
            print('Please input ID number between 1 ~ 10')
            self.userListManage()
        elif userNumber < 0:
            print('Please input ID number between 1 ~ 10')
            self.userListManage()
        elif userNumber == 0:
            self.userLogin()
        else:
            while True:
                inputID = input(f'{userNumber} will be deleted Y/N:')
                if inputID == 'Y' or 'y':
                    for i in range(3):
                        self.userList.insert(self, inputID[userNumber - 1][i], 'Empty')
                    print(f'{inputID} has been deleted')
                    self.userListManage()
                elif inputID == 'N' or 'n':
                    self.userListManage()








