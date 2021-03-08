from User import userInforSet as UIM  #


# 게임 시작화면
# 1: 유저생성, 2: 기존데이터 로드, 3: 기존데이터 관리
while True:
    selection = input("1. New Game\n2. Load Game\n3. User Manager\nSelect menu: ")
    if selection == 1 or 2 or 3:
        UIM.userLogin(selection)
    else:
        continue

# 유저 선택에 따라 게임 난이도 진입


