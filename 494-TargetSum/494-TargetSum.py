# Last updated: 11/26/2025, 5:41:04 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, total):
            if (i, total) not in memo:
                if i >= len(nums):
                    memo[(i, total)] = 1 if total == target else 0
                else:
                    memo[(i, total)] = dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])
            return memo[(i, total)]
        
        return dp(0, 0)