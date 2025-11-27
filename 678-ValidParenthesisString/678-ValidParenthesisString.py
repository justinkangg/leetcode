# Last updated: 11/26/2025, 5:40:55 PM
class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def valid(i, left):
            if (i, left) not in memo:
                if left < 0:
                    return False
                if i == len(s):
                    return left == 0
                elif s[i] == '(':
                    memo[(i, left)] = valid(i + 1, left + 1)
                elif s[i] == ')':
                    memo[(i, left)] = valid(i + 1, left - 1)
                else:
                    memo[(i, left)] = valid(i + 1, left) or valid(i + 1, left + 1) or valid(i + 1, left - 1)
            return memo[(i, left)]

        return valid(0, 0)