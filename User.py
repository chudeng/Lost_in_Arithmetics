# 유저 관리.
# 크게 3가지 기능으로, 유저생성(userCreation), 유저선택(userSelection), 유저관리(userListManage) 기능을 하며,
# 3가지 기능은 userInforSet class로 묶어 두었음.


from UserData import UserData as UD     # # userdata.dat file 관리 라이브러리

class userInforSet:
    # UD library instance 할당
    userData = UD()

    # 새로운 사용자 생성 매서드
    def userCreation(self):
        # userdata.dat 내용을 dict type으로 load
        userDic = self.userData.userLoad()
        while True:
            # 기존 사용자 정보를 userDic에 dict로 할당 후 key와 value는 list로 나눔
            key_List = list(userDic.keys())
            value_List = list(userDic.values())
            for i in range(len(key_List)):
                print(f"ID: {key_List[i]}\t\tLevel: {value_List[i][0]}\tScore: {value_List[i][1]}")

            # 새롭게 생성할 ID type(1자 이상 8자 이하)
            inputID = input(f'============ New User Creation ============\nPlease input ID(Max 8 letters, Quit = -1): ')
            # 입력한게 없거나, 8글자 이상이면 다시 입력.
            if len(inputID) > 8 or len(inputID)<=0:
                continue
            # '-1'이면 유저생성 종료 및 초기화면 복귀
            elif inputID == '-1':
                break
            # 생성요청 ID 검토가 기존 ID와 겹치면 (if true) 다시 입력, 없으면(else) userDic에 key(생성 ID)와 value([0, 0]배열)
            else:
                # ID 대소문자 구분 없음. lower 사용
                emptyID = inputID.lower() in userDic
                # valid생성요청 ID가 숫자와 알페벳으로만 이루어졌는지 판단 여부 변수
                validID = 0
                # 입력ID가 알파벳과 숫자로만 이루어졌으면 validID = True, 아니면 validID = False
                for i in inputID:
                    validID = i.isdigit() or i.isalpha()
                    if not validID == True:
                        break
                    else:
                        pass
                # 입력ID가 기존 ID와 겹치면 다시 입력
                if emptyID == True:
                    print('The ID already used.')
                    continue
                # 입력ID가 알파벳과 숫자로만 이루어지지 않았다면 다시 입력
                elif not validID == True:
                    print('Please input ID with alphabet and numbers.')
                    continue
                # 입력ID의 최종 생성여부 검토
                else:
                    # 'y' or 'Y'이면 self.userDic에 추가 후 UD.userWrite()로 userdata.dat file 에 업데이트 후, 유저생성화면 복귀, 'n' or 'N'이면 업데이트 없이 유저생성화면 복귀.
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
        # 기존 사용자 정보를 userDic에 dict로 할당 후 key와 value로 나누어 list 저장.
        userDic = self.userData.userLoad()
        key_List = list(userDic.keys())
        value_List = list(userDic.values())

        while True:
            # 기존 유저 정보 디스플레이
            for i in range(len(key_List)):
                print(f"ID: {key_List[i]}\t\tLevel: {value_List[i][0]}\tScore: {value_List[i][1]}")
            # -1: 초기화면, 0: 유저관리, others: 선택한 유저로 시작
            ID = input("Please input ID(Back[-1], ID manage[0]): ")
            if ID.lower() == '-1':
                return '-1'
            elif ID == '0':
                self.userListManage()
            else:
                # 기존 유저 정보를 바르게 입력시 ID 및 점수정보(userDic[ID]) 를 리턴, 없는 ID 입력시 유저선택 반복.
                for i in key_List:
                    if ID.lower() == i.lower():
                        return ID, userDic[ID]
                    else:
                        print("Please input right ID")
                        continue



    #사용자 정보 관리(확인 및 삭제)
    def userListManage(self):
        while True:
            # 기존 사용자 정보를 userDic에 dict로 할당 후 key와 value로 나누어 list 저장.
            userDic = self.userData.userLoad()
            key_List = list(userDic.keys())
            value_List = list(userDic.values())
            # 입력한 ID와 기존 ID 비교를 위한 list변수
            key_List_Lower = []
            # 기존 ID 소문자로 변환 후 key_List_Lower에 저장
            for i in key_List:
                key_List_Lower.append(i.lower())
            # 기존 ID 정보 디스플레이
            for i in range(len(key_List)):
                print(f"ID: {key_List[i]}\t\tLevel: {value_List[i][0]}\tScore: {value_List[i][1]}")

            # 삭제할 ID 입력. '-1': 초기화면 복귀
            inputID = input("Please input ID to be deleted(Back[-1]): ")

            if inputID.lower() == '-1':
                break
            # 입력 ID와 기존 ID 일치
            elif inputID.lower() in key_List_Lower:
                # 입력한 ID 삭제 여부 확인. Yes 면 해당 해당 ID 정보 삭제 및 userdata.dat file에 업데이트 후 유저관리 화면 복귀. No면 액션 없이 유저관리 화면 복귀
                while True:
                    confirmation = input(f"{inputID} confirm?(y/n)")
                    if confirmation.lower() == "y":
                        del userDic[inputID.lower()]
                        print(f'{inputID} has been deleted.')
                        self.userData.userWrite(userDic)
                        break
                    elif confirmation == "n" or "N":
                        break
            else:
                print("Please input right ID")
                continue