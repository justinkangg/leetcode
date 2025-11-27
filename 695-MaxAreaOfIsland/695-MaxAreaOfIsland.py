# Last updated: 11/26/2025, 5:40:52 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    q = deque([(r, c)])
                    grid[r][c] = 0
                    curr = 0
                    while q:
                        row, col = q.popleft()
                        curr += 1
                        for new_r, new_c in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                            if (0 <= new_r < m) and (0 <= new_c < n) and grid[new_r][new_c]:
                                grid[new_r][new_c] = 0
                                q.append((new_r, new_c))
                    
                    ans = max(ans, curr)
        return ans