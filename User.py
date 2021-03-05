from UserData import UserData as UD

class userInforSet:
    userData = UD(None)
    def __init__(self, selection):
        self.selection = selection
    # 초기 로그인 화면
    # 유저리스트와 선택 옵션
    def userLogin(self):
        if self.selection == 1:
            self.userCreation()
        elif self.selection == 2:
            self.userSelection()
        elif self.selection == 3:
            self.userListManage()


    # 새로운 사용자 생성 매서드
    def userCreation(self):
        # userdata.dat 내용을 dict type으로 load
        userDic = self.userData.userLoad()
        while True:
            # 새롭게 생성할 ID type(1자 이상 8자 이하)
            inputID = input('==New User Creation==\nPlease input ID(Max 8 letters): ')
            # 입력한게 없거나, 8글자 이상이면 다시 입력.
            if len(inputID) > 8 or len(inputID)<=0:
                continue
            else:
                # 생성요청 ID가 겹치는게 있으면(if true) 다시 입력, 없으면(else) userDic에 key(생성 ID)와 value([0, 0]배열) 추
                emptyID = inputID.lower() in userDic
                print(userDic)
                print(emptyID)
                if emptyID == True:
                    print('The ID already used.')
                    continue
                elif emptyID == 'empty':
                    print('"empty" cannot be used.')
                    continue
                else:
                    # 생성요청한 ID 최종 확인
                    # 'if ture'이면 self.userDic에 추가 후 UD.userWrite()로 userdata.dat file 에 업데이트
                    while True:
                        confirmation = input(f"{inputID} confirm?(y/n)")
                        if confirmation.lower() == "y":
                            userDic.setdefault(inputID, [0,0])
                            self.userData.userWrite(userDic)
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
                key_List = list(self.userDic.keys())
                self.ID = input("Please input ID(Back[-1], ID manage[0]): ")
                if self.ID == -1:
                    self.userLogin()
                elif self.ID == 0:
                    self.userListManage()
                else:
                    for i in key_List:
                        if self.ID == i:
                            return (self.ID, self.userDic.get(self.ID))
                        else:
                            print("Please input right ID")
                            continue


    #사용자 정보 관리(확인 및 삭제)
    def userListManage(self):
        self.userDic = UD.userLoad()
        key_List = list(self.userDic.keys())
        for index, (key, value) in enumerate(self.userDic()):
            print(f"ID: {key}\tLevel: {value[0]}\tScore: {value[1]}\n")
        while True:
            self.ID = input("Please input ID to be deleted(Quit: 0):")
            if self.ID == 0:
                UD.userWrite(self.userDic)
                self.userLogin()
            elif self.ID in key_List:
                del self.userDic[self.ID]
                print(f'{self.ID} has successfully deleted.')
                continue
            else:
                print(f'{self.ID} does not exist. Please input right ID.')
                continue



