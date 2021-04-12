# Score calculator

class scoreCalc:

    def __init__(self, loadedID):
        self._loadedID = loadedID

    # Score calculated with attempt times and times
    def score(self, tryTime, answerTime):
        score = round((self._loadedID[1][0]/tryTime*100) - answerTime, 2) # 점수 변수
        self._loadedID[1][1] = self._loadedID[1][1] + score # 기존 점수에 계산된 score 점수 합산
        if self._loadedID[1][1] >= 100: # 합산된 점수가 100점을 넘으면
            self._loadedID[1][0] += 1   # 레벨 1 상승 하고
            self._loadedID[1][1] = 0    # 점수는 0으로 초기화
            return self._loadedID
        else:
            return self._loadedID
