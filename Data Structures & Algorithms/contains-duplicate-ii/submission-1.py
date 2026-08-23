class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        slide = set()  # window size <= k
        l = 0

        for r in range(len(nums)):
            if r - l  > k:
                slide.remove(nums[l])
                l += 1
            if nums[r] in slide:
                return True
            slide.add(nums[r])
        return False
