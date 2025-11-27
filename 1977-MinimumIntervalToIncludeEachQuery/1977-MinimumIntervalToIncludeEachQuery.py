# Last updated: 11/26/2025, 5:40:25 PM
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        ans = {}
        heap = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heappush(heap, (r - l + 1, l, r))
                i += 1
            
            while heap and heap[0][2] < q:
                heappop(heap)
            ans[q] = heap[0][0] if heap else -1
            
        return [ans[q] for q in queries]

