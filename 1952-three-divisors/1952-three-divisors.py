class Solution:
    def isThree(self, n: int) -> bool:
        l=[]
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        if len(l)==3:
            return True
        else:
            return False

