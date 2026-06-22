class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n

        for i in range(n):
            max_right=-1
            for j in range(i+1, n):
                max_right=max(max_right, arr[j])
            ans[i]=max_right
        return ans