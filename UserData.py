# 유저 정보를 담고 있는 파일 관리
# 업데이트 및 로드 역할.


class UserData:

    # 유저 정보 저장
    # 실행때마다 정보를 덮어 씌움
    # 넘겨받은 userDic 정보를 "userdata.dat(self.UDW)" file 에 print.
    def userWrite(self, userDic):
        with open('userdata.dat', 'w') as UDW:
            print(userDic, file = UDW)


    # 유저 정보 읽어오기
    def userLoad(self):
        with open('userdata.dat', 'r') as UDR:
            # eval을 통해 "userdata.dat(self.UDW)" file 을 읽어올때 'dict' type 으로 읽어옴.
            userDic = eval(UDR.read())
            return (userDic)










