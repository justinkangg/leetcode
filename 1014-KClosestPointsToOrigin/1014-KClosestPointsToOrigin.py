# Last updated: 11/26/2025, 5:40:36 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(sqrt(x**2 + y**2), i) for i, [x, y] in enumerate(points)]
        ans = []
        while k > 0:
            l, r = [], []
            pivot = random.choice(dists)[0]
            for d, i in dists:
                if d <= pivot:
                    l.append((d, i))
                else:
                    r.append((d, i))

            if len(l) <= k:
                ans.extend([points[i] for d, i in l])
                k -= len(l)
                dists = r
            else:
                dists = l
        
        return ans