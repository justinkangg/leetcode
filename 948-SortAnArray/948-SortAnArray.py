# Last updated: 11/26/2025, 5:40:37 PM
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        pivot = random.choice(nums)
        less, equal, more = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                equal.append(num)
        return self.sortArray(less) + equal + self.sortArray(more)

        