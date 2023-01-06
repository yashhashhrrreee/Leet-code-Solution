class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans, max_val = [], float("-inf")

        for xj,yj in points:
            while ans and xj - ans[0][1] > k:
                heapq.heappop(ans)

            if ans:
                max_val = max(max_val,xj+yj-ans[0][0])

            heapq.heappush(ans,(-(yj-xj),xj))

        return max_val
        