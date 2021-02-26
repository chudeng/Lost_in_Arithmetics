class userInforSet:

    def __init__(self, userInitialization, Level, Score):
        self.userInitialization = userInitialization
        self.Level = Level
        self.Score = Score


    # 게임 첫 실행시 10개 유저정보 공간 생성
    def userListCreation(self):
        userList = [['Empty' for j in range(3)] for i in range(10)]
        # 유저 정보를 저장할 파일(userdata.dat) 생성
        with open('userdata.dat', 'w') as SavedUserFile:
            for line in userList:
                for column in userList:
                    SavedUserFile.write(userList[line][column])
                SavedUserFile.write('\n')
        self.userInitialization = 1



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
                break
            else:
                continue


    # 새로운 사용자 생성 매서드
    def userCreation(self):
        # 새로운 사용자를 추가 할 수 있는지 확인
        # 추가 가능시 emptyID에 슬롯 위치를 저장
        emptyID = 0
        for emptyID  in range(10):
            if self.userList[emptyID][0] == "Empty":
                break
            else:
                if emptyID == 9:
                    print("No empty user slot. Check existing user list.")
                    self.userListManage()

        # emptyID 슬롯에 ID 저장 및 기존 ID와 중복여부 검사
        TypedID = input("Input your ID(Max 8 letters): ")
        while True:
            if len(TypedID) > 8:
                TypedID = input("Please input ID(Max 8 letters)")
                continue
            elif len(TypedID) == 0:
                TypedID = input("Please input ID(Max 8 letters)")
                continue
            else:
                break

        for i in range(10):
            if TypedID == self.userList[i][0]:
                TypedID = input("Already used ID. Input your ID(Max 8 letters): ")
            else:
                if i == 9:
                    while True:
                        confirmationID = input(f"{TypedID} confirm?(y/n)")
                        if confirmationID == "y" or "Y":
                            self.userList[emptyID][0] = TypedID
                            break
                        elif confirmationID == "n" or "N":
                            self.userCreation()



    # 사용자 정보 확인
    # 기존 사용자이면, 해당 정보 로드
    # 새로운 사용자이면, 사용자생성(userCreation) 매서드 호출
    def userSelection(self):
        for i in range(10):
            print(f"{i + 1} ':' {self.userList[i]}\n")
        while True:
            self.ID = input("Please input ID number(Back[-1], ID manage[0]): ")
            if self.ID == -1:
                self.userLogin()
            elif self.ID == 0:
                self.userListManage()
            elif self.ID <0:
                self.userSelection()
            elif self.ID >10:
                self.userSelection()
            else
                return self.ID


    #사용자 정보 관리(확인 및 삭제)
    def userListManage(self):
        for i in range(10):
            print(f"{i+1} ':' self.userList[i]\n")
        userNumber = int(input("Please input ID number to be deleted(Quit: 0):"))
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








