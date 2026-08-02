class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {} # value -> index

        for i, value in enumerate(nums):
            diff =target - value

            if diff in ans:
                return [ans[diff], i]
            ans[value] = i
