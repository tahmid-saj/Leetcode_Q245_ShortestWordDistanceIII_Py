class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res, pos1, pos2 = math.inf, -1, -1
        for i in range(len(wordsDict)):
            if word1 == word2 and wordsDict[i] == word1:
                if pos1 == -1 and pos2 == -1: pos1 = i
                elif pos2 < pos1: pos2 = i
                else: pos1 = i
            else:
                if wordsDict[i] == word1: pos1 = i
                elif wordsDict[i] == word2: pos2 = i
            if pos1 != -1 and pos2 != -1: res = min(res, abs(pos1 - pos2))
        return res
