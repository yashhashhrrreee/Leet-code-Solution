class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Traverse all elements through the loop...
        for i in range(len(nums)):
            if(nums[i] >= target):
                return i
        return len(nums)