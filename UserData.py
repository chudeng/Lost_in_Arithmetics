from User import userInforSet as UIM  #User.py module 사용
from User.userInforSet import userListCreation as ULC

class UserData:

    def __init__(self, userData, num, ID, level, score, UDF):
        self.userData = userData
        self.num = num
        self.ID = ID
        self.level = level
        self.score = score


    # 변경된 유저 정보를 저장
    def userUpdate(self, num, ID, level, score):
        self.userData = [ID, level, score]
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










