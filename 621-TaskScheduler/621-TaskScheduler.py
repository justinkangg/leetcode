# Last updated: 11/26/2025, 5:40:56 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapify(heap)
        q = deque()
        while heap or q:
            time += 1
            if heap:
                count = heappop(heap)
                if count + 1:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0] + 1)
        return time