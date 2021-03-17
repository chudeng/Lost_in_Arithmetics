from User import userInforSet as UIM
from UserData import UserData as UD
from Game import game
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
loadedID = []
while True:
    gamemode = input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: ")
    if gamemode == '1':
        gameMenu.userCreation()
        continue
    elif gamemode == '2':
        loadedID = gameMenu.userSelection()
        if loadedID == '-1':
            continue
        else:
            break
    elif gamemode == '3':
        gameMenu.userLogin(gamemode)
        continue
    else:
        continue

print(loadedID, type(loadedID))
# 로드된 유저 정보에 맞는 게임 시작
gamestart = game(list(loadedID))

print(gamestart)