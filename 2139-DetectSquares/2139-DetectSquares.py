# Last updated: 11/26/2025, 5:40:26 PM
class DetectSquares:
    def __init__(self):
        self.points = Counter()
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1


    def count(self, point: List[int]) -> int:
        ans = 0
        qx, qy = point
        for (x, y) in self.points:
            if qx != x and qy != y and abs(qx - x) == abs(qy - y):
                ans += self.points[(x, y)] * self.points[(qx, y)] * self.points[(x, qy)]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)