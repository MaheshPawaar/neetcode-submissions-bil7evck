class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp={}
        for i in range(len(nums)):
            ans=target-nums[i]
            if ans in tmp:
                return [tmp[ans],i]
            tmp[nums[i]]=i
        return [-1,-1]