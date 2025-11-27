# Last updated: 11/26/2025, 5:40:55 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            for left, right in [(i, i), (i, i + 1)]:
                while (0 <= left < n) and (0 <= right < n):
                    if s[left] != s[right]:
                        break
                    count += 1
                    left -= 1
                    right += 1
        
        return count