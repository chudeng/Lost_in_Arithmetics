# 프로그램의 메인 모듈

from User import userInforSet as UIM    # user 관리 라이브러리
from UserData import UserData as UD     # userdata.dat file 관리 라이브러리
from Game import game                   # 게임 수행 라이브러리
from score import scoreCalc             # 유저의 레벨 및 점수 관리 라이브러리
import os                               # userdata.dat file 생성 여부 확인을 위한 라이브러리

# UD, UIM library instance 할당
gameInit = UD()
gameMenu = UIM()

# userdata.dat 파일이 있으면 패스, 없으면 생성 및 초기화
datfile = os.path.isfile('userdata.dat')
if datfile == False:
    userInitDic = {}
    gameInit.userWrite(userInitDic)
else:
    pass

# loadedID: 유저 정보를 담을 list
loadedID = []
# 3개의 게임 시작 모드 외의 입력은 무시 및 시작화면 반복.
while True:
    # 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리
    gamemode = input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: ")
    if gamemode == '1': # 유저생성 -> User.py -> userCreation
        gameMenu.userCreation()
        continue
    elif gamemode == '2': # 유저선택 -> User.py -> userSelection
        loadedID = gameMenu.userSelection()
        if loadedID == '-1':    # 유저선택이 '-1'이면 초기화면 복귀
            continue
        else:   # loadedID에 선택 유저정보 저장
            loadedID = list(loadedID)
            # 로드된 유저 정보를 game과 scoreClac class에 전달
            gameScore = scoreCalc(loadedID)
            userGameSet = game(loadedID)
            # game 수행 -> Game.py -> stage()
            while True:
                gamePlay = userGameSet.stage()
                # 게임중 종료 또는 계속 여부 확인: '-1'이면 종료 및 초기화면 복귀. 그 외 게임 계속 진행
                if gamePlay == '-1':
                    break
                else:
                    continue
            continue
    elif gamemode == '3':   # 유저정보 관리 -> User.py -> userListManage
        gameMenu.userListManage()
        continue
    else:   # 세가지 메뉴 외 선택시, 다시 초기 화면
        continue


