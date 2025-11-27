# Last updated: 11/26/2025, 5:40:40 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        times = [(target - p) / s for p, s in cars]

        stack = []
        for t in times:
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)