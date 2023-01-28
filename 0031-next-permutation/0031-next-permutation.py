class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a,b):
            nums[a],nums[b] = nums[b],nums[a]
            return
        def reverse(i):
            nums[i:] = nums[i:][::-1]
            
        if len(nums) <= 1:
            return 
        j = len(nums)-1
        while(j>=0 and nums[j-1] >= nums[j]):
            j-=1
        j-=1
        # Find the end of the non decreasing part of the array
        while(j>=0):
            i = j+1
            while(i<len(nums) and nums[j]<nums[i]):
                i+=1
            swap(i-1,j)
            #Swap with next greatest element on the right side
            break
        reverse(j+1)
        # Reverse the non increasing part
        return