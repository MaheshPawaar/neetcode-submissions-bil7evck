class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {} # ele -> index

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nMap:
                return [nMap[diff], i]
            nMap[nums[i]]=i
        return [-1,-1]