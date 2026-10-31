class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r=0, len(height)-1
        res=0

        while l < r:
            width=r-l
            water=min(height[l], height[r]) *width
            res=max(res, water)

            if (height[l] < height[r]):
                l+=1
            else:
                r-=1
        return res