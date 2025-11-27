# Last updated: 11/26/2025, 5:40:58 PM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges) + 1))

        def find(u):
            if parents[u] == u:
                return u
            return find(parents[u])
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return True
            parents[pu] = pv
            return False
        
        ans = []
        for u, v in edges:
            if union(u, v):
                ans = [u, v]
        return ans
        