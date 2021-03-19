postNo = input('우편번호:')
if postNo[2] == '0' or postNo[2] == '1' or postNo[2] == '2':
    print('강북구')
elif postNo[2] == '3' or postNo[2] == '4' or postNo[2] == '5':
    print('도봉구')
else:
    print('노원구')