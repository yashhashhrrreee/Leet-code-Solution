class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        if n < 5:
            return 0
        while n >= 5 :
            count += int(n/5) 
            n = int(n/5) 
        return count
        