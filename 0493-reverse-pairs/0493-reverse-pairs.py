from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_list = SortedList()
        ans = 0
        for n in nums:
            target = n*2
            pos = bisect.bisect_right(sorted_list, target)
            # If pos == len(sorted_list), target is too large
            ans += len(sorted_list)-pos
            
            sorted_list.add(n)
        
        return ans