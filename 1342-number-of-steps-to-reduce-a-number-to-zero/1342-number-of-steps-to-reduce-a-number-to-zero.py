class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        n=num
        while n!=0:
            if n%2==0:
                n/=2
            else:
                n-=1
            c+=1   
        return c

        