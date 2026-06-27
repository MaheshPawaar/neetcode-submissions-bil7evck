class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={} # val -> frequency
        ans=[]

        for num in nums:
            frequency[num] = 1 + frequency.get(num,0)
        
        ans=[]
        
        for num, cnt in frequency.items():
            ans.append([cnt, num])
        ans.sort()

        res = []
        while len(res) < k:
            res.append(ans.pop()[1])
        return res        
        