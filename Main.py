from User import userInforSet as UIM  #
from UserData import UserData as UD
import os

class main:

    def __init__(self, selection):
        self.selection = selection

    def userLogin(self):
        # 게임 시작화면
        # 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리
        while True:
            self.selection = int(input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: "))
            if self.selection == 1 or self.selection == 2 or self.selection == 3:
                pass
            else:
                continue

gameInit = UD(None)
gameMenu = UIM(None)

datFile = os.path.isfile('/Lost_in_Arithmetics/userdata.dat')
if datFile == False:
    userInitDic = {'Empty':[0, 0]}
    gameInit.userWrite(userInitDic)
else:
    pass

while True:
    gameMenu.selection = int(input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: "))
    gamemode = gameMenu.selection
    if gamemode == 1 or gamemode == 2 or gamemode == 3:
        gameMenu.userLogin()
    else:
        continue
