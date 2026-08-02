class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        f=""
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                f+=s[i]
                i+=1
                j+=1
            else:
                j+=1
        if f==s:
            return True
        else:
            return False




        