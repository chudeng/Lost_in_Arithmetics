RRN = input('주민등록번호:')
RRN = RRN.split('-')
RRN = list(''.join(RRN))
print(RRN)
key = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
sum = 0

for i in range(12):
    sum = sum + (int(RRN[i]) * int(key[i]))
    print(sum, sum%11)
print(sum)
if 11 - (sum%11) == RRN[12]:
    print('유효한 주민등록 번호 입니다.')
else:
    print('유효하지 않은 주민등록 번호 입니다.')