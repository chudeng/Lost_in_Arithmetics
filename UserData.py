from User import userInforSet as UIM  #User.py module 사용
from User.userInforSet import userListCreation as ULC

class UserData:

    def __init__(self, userData, num, ID, level, score, UDF):
        self.userData = userData
        self.num = num
        self.ID = ID
        self.level = level
        self.score = score
    UDWrite = open('userdata.txt', 'w')


    # 유저 데이터 정보를 보관할 파일 생성
    def userdataFileUpdate(self):
        self.userData = ULC.userList
        for line in range(10):
            self.UDWrite.write((line + 1) + '. ')
            for column in range(2):
                self.UDWrite.write(self.userData[line][column] + '   ')
            self.UDWrite.close()
            self.UDWrite.write("\n")
        self.UDWrite.close()


    # 변경된 유저 정보를 저장
    def userWrite(self, num, ID, level, score):
        userUpdate = [ID, level, score]
        for line in self.userData:
            if self.userData[line] == num - 1:
                for column in self.userData:
                    self.userData[line][column] = userUpdate[column]
        self.userdataFileUpdate()


    # 유저 정보 읽어오기
        def userLoad(self, num):
            userLoaded = [ID, level, score]
            for line in self.userData:
                if self.userData[line] == num - 1:
                    for column in self.userData:
                        self.userData[line][column] = userLoaded[column]
            return userLoaded










