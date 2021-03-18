userPhoneNumber = input('휴대전화 번호 입력:')
telecomDict = {'011':'당신은 SKT 사용자입니다.', '016':'당신은 KT 사용자입니다.', '019':'당신은 LGU 사용자입니다.', '010':'알수없는 통신사 사용자입니다.'}
num = userPhoneNumber[0:3]
print(telecomDict[num])