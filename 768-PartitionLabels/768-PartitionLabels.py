# Last updated: 11/26/2025, 5:40:47 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lasts = {}
        for i, c in enumerate(s):
            lasts[c] = i
        
        ans = []
        curr = r = 0
        for l, c in enumerate(s):
            curr += 1
            r = max(r, lasts[c])
            if l == r:
                ans.append(curr)
                curr = 0
        return ans
