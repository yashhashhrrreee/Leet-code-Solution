class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(nums, target, flag):
            output=-1
            
            start= 0
            end= len(nums)-1
            
            while start <= end :
                mid = (start + end) // 2
                
                if nums[mid] > target :
                    end = mid - 1
                    
                elif nums[mid] < target :
                    start = mid + 1
                
                else:
                    if flag is True:
                        output=mid
                        end= mid-1
                    else:
                        output= mid
                        start= mid+1
            return output
        return [binarysearch(nums, target, True), binarysearch(nums, target, False)]
        