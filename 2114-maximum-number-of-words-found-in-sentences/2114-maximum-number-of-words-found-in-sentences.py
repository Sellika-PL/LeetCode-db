class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0

        for i in sentences:
            count = len(i.split())
            maxi = max(maxi, count)

        return maxi


        