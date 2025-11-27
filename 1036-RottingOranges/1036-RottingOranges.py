# Last updated: 11/26/2025, 5:40:34 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                    ans = -1
        
        while q:
            ans += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for new_r, new_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                    if (0 <= new_r < m) and (0 <= new_c < n) and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return ans