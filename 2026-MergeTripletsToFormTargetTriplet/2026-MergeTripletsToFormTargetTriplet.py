# Last updated: 11/26/2025, 5:40:27 PM
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = [t for t in triplets if all(x <= y for x, y in zip(t, target))]

        return bool(candidates) and (list(max(values) for values in zip(*candidates)) == target)