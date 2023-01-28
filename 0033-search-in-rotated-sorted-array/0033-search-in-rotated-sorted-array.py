class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r   = 0, len(nums) - 1
        left_v = nums[0]
        
        while l < r:
            m     = (l + r) // 2
            m_val = nums[m]

            if   m_val <  left_v <= target:  r = m - 1
            elif m_val >= left_v >  target:  l = m + 1 
            elif m_val <  target:            l = m + 1
            elif m_val >  target:            r = m - 1
            else:                            return m
                    
        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1
