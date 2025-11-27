# Last updated: 11/26/2025, 5:40:44 PM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #dijkstras
        n = len(grid)
        heap = []
        heappush(heap, (grid[0][0], 0, 0))
        visited = {(0, 0)}
        while heap:
            t, r, c = heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            for new_r, new_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if (0 <= new_r < n) and (0 <= new_c < n) and ((new_r, new_c) not in visited):
                    visited.add((new_r, new_c))
                    heappush(heap, (max(grid[new_r][new_c], t), new_r, new_c))
        return -1

