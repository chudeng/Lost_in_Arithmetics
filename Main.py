from User import userInforSet as UIM
from UserData import UserData as UD
import os

# UD, UIM instance 할당
gameInit = UD()
gameMenu = UIM()

# userdata.dat 파일이 있으면 패스, 없으면 생성 및 초기화
datfile = os.path.isfile('/Lost_in_Arithmetics/userdata.dat')
if datfile == False:
    userInitDic = {}
    gameInit.userWrite(userInitDic)
else:
    pass

# 게임 시작화면
# 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리
while True:
    gamemode = int(input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: "))
    if gamemode == 1:
        gameMenu.userCreation()
        continue
    elif gamemode == 2:
        gameMenu.userSelection()
        break
    elif gamemode == 3:
        gameMenu.userLogin(gamemode)
        continue
    else:
        continue

print('게임 짜자')