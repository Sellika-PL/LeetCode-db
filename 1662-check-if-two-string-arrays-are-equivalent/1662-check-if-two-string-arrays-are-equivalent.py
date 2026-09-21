class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s1=""
        s2=""
        for i in word1:
            s1+=i
        for i in word2:
            s2+=i
        if s1==s2:
            return True
        else:
            return False
        
        