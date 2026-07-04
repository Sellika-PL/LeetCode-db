class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        f=[]
        for i in nums:
            s=i*i
            f.append(s)
        f.sort()
        return f