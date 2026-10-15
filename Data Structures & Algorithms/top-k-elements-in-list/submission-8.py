class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={} # freq -> ele

        for num in nums:
            freq[num]=1+freq.get(num, 0)

        res=[]
        for ele, cnt in freq.items():
            res.append([cnt, ele])
        res.sort()

        ans=[]
        while len(ans)<k:
            ans.append(res.pop()[1])
        return ans