class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(i, cur):
                        
            if sum(cur)  > n  or len(cur)  > k:    
                return
            if sum(cur) == n and len(cur) == k: 
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):      
                el = nums[j]                    
                dfs(j + 1, cur + [el])       

        res    = []
        nums   = [i   for i in range(1, 10)]   
        dfs(0, [])

        return res