class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        for i in range(0,len(costs)):
            coins=coins-costs[i]
            if(coins<0):
                return i
            if(coins==0):
                return i+1
        return i+1