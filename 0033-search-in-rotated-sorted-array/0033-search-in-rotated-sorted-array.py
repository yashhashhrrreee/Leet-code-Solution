class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        g = nums
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        nums = sorted(nums)
        start = 0
        end = len(nums)
        while start < end:
            m = (end+start) // 2
            print (m)
            if nums[m] == target:
                try:
                    return g.index(nums[m])
                except ValueError:
                    return -1
            if nums[m] < target:
                start = m + 1
            if nums[m] > target:
                end = m
        return -1