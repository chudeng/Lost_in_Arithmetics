from User import userInforSet as UIM    #
from UserData import UserData as UD     # UserData.py 의 Userdate impor


# 게임 시작화면
# 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리

while True:
    UIM.userLogin(None)
    if 1:
        UIM.userCreation(None)
    elif UIM.userLogin(None) == 2:
        UIM.userSelection(None)
    elif UIM.userLogin(None) == 3:
        UIM.userListManage(None)
    else:
        continue


# 유저 선택에 따라 게임 난이도 진입



