# Last updated: 11/26/2025, 5:41:01 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        counts[0] = 1
        rolling = 0
        ans = 0
        for num in nums:
            rolling += num
            ans += counts[rolling - k]
            counts[rolling] += 1
        return ans