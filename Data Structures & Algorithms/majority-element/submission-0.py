class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap=defaultdict(int) # num -> count
        res = maxCount=0

        for num in nums:
            countMap[num] += 1
            if maxCount < countMap[num]:
                res = num
                maxCount=countMap[num]
        return res
            
        
