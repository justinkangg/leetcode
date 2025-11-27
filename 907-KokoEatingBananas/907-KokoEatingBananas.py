# Last updated: 11/26/2025, 5:40:41 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            curr = 0
            for pile in piles:
                curr += math.ceil(pile / k)
            if curr > h:
                l = k + 1
            else:
                r = k
        return l