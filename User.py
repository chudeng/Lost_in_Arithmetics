from UserData import UserData as UD

class userInforSet:

    userData = UD()

    # 새로운 사용자 생성 매서드
    def userCreation(self):
        # userdata.dat 내용을 dict type으로 load
        userDic = self.userData.userLoad()
        while True:
            # 기존 사용자 정보를 userDic에 dict로 할당 후 key와 value는 list로 나눔
            userDic = self.userData.userLoad()
            key_List = list(userDic.keys())
            value_List = list(userDic.values())
            for i in range(len(key_List)):
                print(f"ID: {key_List[i]}\t\tLevel: {value_List[i][0]}\tScore: {value_List[i][1]}")

            # 새롭게 생성할 ID type(1자 이상 8자 이하)
            inputID = input(f'============ New User Creation ============\nPlease input ID(Max 8 letters, Quit = -1): ')
            # 입력한게 없거나, 8글자 이상이면 다시 입력.
            if len(inputID) > 8 or len(inputID)<=0:
                continue
            elif inputID == '-1':
                break
            else:
                # 생성요청 ID가 겹치는게 있으면(if true) 다시 입력, 없으면(else) userDic에 key(생성 ID)와 value([0, 0]배열) 추
                emptyID = inputID.lower() in userDic
                vaildID = 0
                for i in inputID:
                    vaildID = i.isdigit() or i.isalpha()
                    if not vaildID == True:
                        break
                    else:
                        pass
                if emptyID == True:
                    print('The ID already used.')
                    continue
                elif not vaildID == True:
                    print('Please input ID with alphabet and numbers.')
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
                            userDic.setdefault(inputID, [1,0])
                            self.userData.userWrite(userDic)
                            break
                        elif confirmation == "n" or "N":
                            self.userCreation()
                            break


    # 사용자 정보 확인
    # 기존 사용자이면, 해당 정보 로드
    # 새로운 사용자이면, 사용자생성(userCreation) 매서드 호출
    def userSelection(self):
        # 기존 사용자 정보를 userDic에 dict로 할당 후 key와 value는 list로 나눔
        userDic = self.userData.userLoad()
        key_List = list(userDic.keys())
        value_List = list(userDic.values())

        while True:
            for i in range(len(key_List)):
                print(f"ID: {key_List[i]}\t\tLevel: {value_List[i][0]}\tScore: {value_List[i][1]}")
            ID = input("Please input ID(Back[-1], ID manage[0]): ")
            # -1: 초기화면, 0: 유저관리, others: 선택한 유저로 시작
            if ID.lower() == '-1':
                return '-1'
            elif ID == '0':
                self.userListManage()
            else:
                for i in key_List:
                    if ID.lower() == i.lower():
                        return ID, userDic[ID]
                    else:
                        print("Please input right ID")
                        continue



    #사용자 정보 관리(확인 및 삭제)
    def userListManage(self):
        while True:
            # 기존 사용자 정보를 userDic에 dict로 할당 후 key와 value는 list로 나눔
            userDic = self.userData.userLoad()
            key_List = list(userDic.keys())
            value_List = list(userDic.values())
            # 입력한 ID와 key값을 비교하기 위한 key 값 소문자화 배열
            key_List_Lower = []
            for i in key_List:
                key_List_Lower.append(i.lower())
            for i in range(len(key_List)):
                print(f"ID: {key_List[i]}\t\tLevel: {value_List[i][0]}\tScore: {value_List[i][1]}")

            inputID = input("Please input ID to be deleted(Back[-1]): ")

            if inputID.lower() == '-1':
                break
            elif inputID.lower() in key_List_Lower:
                while True:
                    confirmation = input(f"{inputID} confirm?(y/n)")
                    if confirmation.lower() == "y":
                        del userDic[inputID.lower()]
                        print(userDic)
                        self.userData.userWrite(userDic)
                        break
                    elif confirmation == "n" or "N":
                        break
            else:
                print("Please input right ID")
                continue