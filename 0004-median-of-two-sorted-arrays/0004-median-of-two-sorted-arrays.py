class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1+nums2)
        l = len(num)
        if l%2!=0:
            return num[int(l/2)]
        else:
            return (num[int(l/2)] + num[int((l/2))-1])/2
        