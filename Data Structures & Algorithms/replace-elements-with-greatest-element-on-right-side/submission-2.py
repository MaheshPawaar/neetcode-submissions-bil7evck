class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n

        max_right=-1
        for i in range(n-1, -1, -1):
           ans[i]=max_right
           max_right=max(arr[i], max_right)
        return ans