# Last updated: 11/26/2025, 5:40:33 PM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            heappush(heap, heappop(heap) - heappop(heap))
        return -heap[0]