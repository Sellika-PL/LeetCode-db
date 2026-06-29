class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            h = min(height[l], height[r])
            area = width * h

            max_area = max(max_area, area)

            # Move the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


        