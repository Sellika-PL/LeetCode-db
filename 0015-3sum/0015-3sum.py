class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''i=0
        j=1
        k=2
        l=[]
        while k<len(nums):
            if nums[i]+nums[j]+nums[k]==0:
                l.append([nums[i],nums[j],nums[k]])
            i+=1
            j+=1
            k+=1
        unique_list = list(set(map(tuple, l))) 
        return unique_list  '''
    
        nums.sort()
        ans = []

        i = 0
        while i < len(nums) - 2:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1          # left pointer
            k = len(nums) - 1  # right pointer

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < 0:
                    j += 1

                else:
                    k -= 1

            i += 1

        return ans


        