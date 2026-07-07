class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l=list(map(int,str(n)))
        y=[]
        for i in l:
            if i!=0:
                y.append(i)
        s=sum(y)
        if len(y)==0:
            return 0
        x=int(''.join(map(str,y)))
        return s*x
        
        