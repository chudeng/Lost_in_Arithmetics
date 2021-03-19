from User import userInforSet as UIM
from UserData import UserData as UD
from Game import game
from score import scoreCalc
import os

# UD, UIM instance 할당
gameInit = UD()
gameMenu = UIM()

# userdata.dat 파일이 있으면 패스, 없으면 생성 및 초기화
datfile = os.path.isfile('userdata.dat')
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
    if gamemode == '1': # 유저생성
        gameMenu.userCreation()
        continue
    elif gamemode == '2':
        loadedID = gameMenu.userSelection()
        if loadedID == '-1':    # 초기화면
            continue
        else:   # list type으로 선택 유저정보 저장
            loadedID = list(loadedID)
            # 로드된 유저 정보를 game과 scoreClac class에 전달
            gameScore = scoreCalc(loadedID)
            userGameSet = game(loadedID)
            # game 수행
            while True:
                gamePlay = userGameSet.stage()
                print(loadedID, gamePlay)
                if gamePlay == '-1':
                    break
                else:
                    continue
            continue
    elif gamemode == '3':   # 유저정보 관리
        gameMenu.userLogin(gamemode)
        continue
    else:   # 세가지 메뉴 외 선택시, 다시 초기 화면
        continue


