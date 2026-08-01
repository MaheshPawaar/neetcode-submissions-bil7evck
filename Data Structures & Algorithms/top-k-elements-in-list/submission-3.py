class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        heap=[]
        for num in frequency.keys():
            heapq.heappush(heap,(frequency[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res