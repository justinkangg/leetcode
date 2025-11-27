# Last updated: 11/26/2025, 5:40:51 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
        return ans