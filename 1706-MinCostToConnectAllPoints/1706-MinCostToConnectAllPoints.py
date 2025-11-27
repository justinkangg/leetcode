# Last updated: 11/26/2025, 5:40:27 PM
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = []
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges = deque(sorted(edges))
        
        parents = list(range(n))

        def find(u):
            if parents[u] == u:
                return u
            return find(parents[u])
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parents[pu] = parents[pv]
            return True

        ans = 0
        count = 0
        while edges and count < n - 1:
            dist, i, j = edges.popleft()
            if union(i, j):
                ans += dist
                count += 1
        return ans