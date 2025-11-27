# Last updated: 11/26/2025, 5:40:49 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:2]
        cost.append(0)

        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[-1], dp[-2]))
        
        return dp[-1]