# Last updated: 11/26/2025, 5:40:49 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = [float('inf')] * n
        dists[k - 1] = 0
        for i in range(n):
            for u, v, w in times:
                if dists[u - 1] != float('inf') and dists[u - 1] + w < dists[v - 1]:
                    dists[v - 1] = dists[u - 1] + w
                    if i == n - 1:
                        return -1 #negative loop that cannot happen here
        
        time = max(dists)
        return -1 if time == float('inf') else time