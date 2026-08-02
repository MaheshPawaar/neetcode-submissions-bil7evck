class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}  # cur_sum -> No. of times it appeared
        cur_sum = 0
        count = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            prefix_sums[cur_sum] = 1+prefix_sums.get(cur_sum,0)
        return count
