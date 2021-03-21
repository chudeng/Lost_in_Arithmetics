# Score calculator

class scoreCalc:

    def __init__(self, loadedID):
        self._loadedID = loadedID

    # Score calculated with attempt times and times
    def score(self, tryTime, answerTime):
        score = round((self._loadedID[1][0]/tryTime*100) - answerTime, 2)
        self._loadedID[1][1] = self._loadedID[1][1] + score
        if self._loadedID[1][1] >= 100:
            self._loadedID[1][0] += 1
            self._loadedID[1][1] = 0
            return self._loadedID
        else:
            return self._loadedID
