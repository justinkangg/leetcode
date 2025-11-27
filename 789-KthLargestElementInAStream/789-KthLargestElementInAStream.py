# Last updated: 11/26/2025, 5:40:46 PM
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        self.k -= 1

        if self.k < 0:
            heappop(self.heap)
            self.k += 1

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)