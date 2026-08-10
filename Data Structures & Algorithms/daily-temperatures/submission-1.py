class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []  # pair: [val, index]

        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackVal, stackIndex = stack.pop()
                ans[stackIndex] = index - stackIndex
            stack.append((val, index))
        return ans
