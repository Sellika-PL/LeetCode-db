class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul=1
        for i in nums:
            mul*=i

        if mul>0:
            return 1
        elif mul<0:
            return -1
        else:
            return 0

        