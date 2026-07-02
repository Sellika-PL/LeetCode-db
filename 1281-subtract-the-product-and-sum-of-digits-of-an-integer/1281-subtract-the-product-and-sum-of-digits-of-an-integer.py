class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums=list(map(int,str(n)))
        sum=0
        prod=1
        for i in nums:
            sum+=i
        for i in nums:
            prod*=i
        return prod-sum
        