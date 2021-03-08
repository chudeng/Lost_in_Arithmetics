from User import userInforSet as UIS
from UserData import UserData as UD
import os.path

# player 정보
player = {'empty': [0, 0]}

# UIS, UD class instance 선언
User = UIS()
UserData = UD()

# 유저정보를 저장할 파일 생성. 생성이 되어 있으면 패스
userDatafile = os.path.isfile('userdata.dat')
if userDatafile == True:
    pass
else:
    UserData.userWrite(player)

print(UserData.userLoad())

# 게임 시작화면
# 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리
while True:
    selection = int(input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: "))
    if selection == 1 or 2 or 3:
        player = User.userLogin(selection)
    else:
        continue

# 유저 선택에 따라 게임 난이도 진입


