# Last updated: 11/26/2025, 5:40:43 PM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        hand.sort()
        for h in hand:
            if counter[h] > 0 and not counter[h - 1]:
                for i in range(groupSize):
                    if not counter[h + i]:
                        return False
                    counter[h + i] -= 1
        return True
