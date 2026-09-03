class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in sentences:
            c=len(i.split())
            if max<c:
                max=c
        return max




        