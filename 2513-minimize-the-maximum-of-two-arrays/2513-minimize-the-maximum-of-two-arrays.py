class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        # Helper function to check if a given value x satisfies the conditions
        def isGood(x):
            nonlocal divisor1, divisor2
            
            # Calculate the number of elements that cannot be used to fill either arr1 or arr2 within the range [1, x]
            dontUseFirst = x // divisor1
            dontUseSecond = x // divisor2
            
            # Calculate the number of elements that cannot be used in either arrays due to their least common multiple (lcm)
            dontUseBoth = x // math.lcm(divisor1, divisor2)
            
            # Check if there are enough elements in the range of positive integers bounded by x to satisfy length requirements
            if x - dontUseBoth < uniqueCnt1 + uniqueCnt2:
                return False
            elif x - dontUseFirst < uniqueCnt1: 
                return False
            elif x - dontUseSecond < uniqueCnt2:
                return False
            else:
                return True 
        
        # Define the left and right bounds of the search space for binary search
        left, right = 1, 10 ** 12
        ans = None
        
        # Perform binary search on the range [left, right]
        while left <= right:
            mid = (left + right) // 2
            res = isGood(mid)
            
            # If the mid-value candidate upholds the condition, explore the left half of the search space
            if res:
                ans = mid
                right = mid - 1
            else:
                # If the mid-value candidate does not uphold the condition, explore the right half of the search space
                left = mid + 1
                
        # Return the final answer
        return ans