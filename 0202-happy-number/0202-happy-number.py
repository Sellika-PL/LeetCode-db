class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        while n not in l:
            l.append(n)
            li=list(map(int,str(n)))
            tot=0
            for i in li:
                tot+=i**2
            n=tot
            if n==1:
                return True
        return False

                    
    

        



        