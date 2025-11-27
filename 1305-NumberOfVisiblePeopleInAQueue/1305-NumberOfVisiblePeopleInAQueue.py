# Last updated: 11/26/2025, 5:40:30 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []
        
        for i in reversed(range(n)):
            h = heights[i]
            while stack and stack[-1] < h:
                stack.pop()
                ans[i] += 1
            if stack: #differentiate between if there is a last person we see or just empty space
                ans[i] += 1
            stack.append(h)
        return ans