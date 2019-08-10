# Pair contains word and it's frequency, compare by frequency
class Pair:
    def __init__(self, word):
        self.word = word
        self.freq = 1

    def __gt__(self, other):
        return self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def getWord(self):
        return self.word

    def getFreq(self):
        return self.freq

    def setFreq(self, freq):
        self.freq = freq

    def addFreq(self, x=1):
        self.freq += x


# Return index of word in list
def find(list, word):
    for item in range(0, len(list)):
        if word == list[item].getWord():
            return item
    return -1
