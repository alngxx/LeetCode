class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # List of all words
        word = sentence.split()

        for i in range(1, len(word)):
            if word[i][0] != word[i - 1][-1]:
                return False

        if word[0][0] != word[-1][-1]:
            return False

        return True
