class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul=1
        for i in nums:
            mul*=i
        return self.signFunc(mul)

    def signFunc(self,X):
        if X>0:
            return 1
        elif X<0:
            return -1
        else:
            return 0

        