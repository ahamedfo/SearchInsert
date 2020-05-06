class Solution(object):
    def searchInsert(self, nums, target):
        for idx, number in enumerate(nums):
            if target <= number:
                return idx
        return len(nums)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
