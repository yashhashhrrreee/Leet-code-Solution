class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not (low & 1 and high & 1):
            return len(range(low,high+1)) // 2
        else:
            return len(range(low,high+1)) // 2 + 1
        