class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        if len(points) == 1:
            return 1
        count = 1
        curmax = max(points[0])
        for baloon in points[1:]:
            if min(baloon)>curmax:
                count+=1
                curmax = max(baloon)
        return count