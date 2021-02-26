from User import userInforSet as UIM    #
from UserData import UserData as UD     # UserData.py 의 Userdate import
import Game

# UserList 생성.
# 모듈 첫 수행시에만 수행
if UIM.__init__(userInitialization=0):
    UIM.userListCreation()
else:
    pass

# 게임 시작화면
# 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리
UIM.userLogin()
if UIM.userLogin() == 1:
    UIM.userCreation()
elif UIM.userLogin() == 2:
    UIM.userSelection()
elif UIM.userLogin() == 3:
    UIM.userListManage()


# 유저 선택에 따라 게임 난이도 진입
for level in UD.



