# Last updated: 11/26/2025, 5:40:59 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        counter1 = Counter(s1)
        counter2 = Counter(s2[:n])
        matches = 0
        for c in string.ascii_lowercase:
            if counter1[c] == counter2[c]:
                matches += 1

        l = 0
        for r in range(n, len(s2)):
            if matches == 26:
                return True

            c = s2[r]
            counter2[c] += 1
            if counter2[c] == counter1[c]:
                matches += 1
            elif counter2[c] == counter1[c] + 1:
                matches -= 1
            
            c = s2[l]
            counter2[c] -= 1
            if counter2[c] == counter1[c]:
                matches += 1
            elif counter2[c] == counter1[c] - 1:
                matches -= 1

            l += 1   
        return matches == 26
                