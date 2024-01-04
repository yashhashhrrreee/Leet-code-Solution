class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        queue = deque()
        heights = [[None]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    queue.append((r, c, 0))
                    heights[r][c] = 0
        
        while queue:
            r, c, dis = queue.popleft()
            
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            for i, j in directions:
                currR, currC = r+i, c+j
                if 0<= currR < ROWS and 0 <= currC < COLS and heights[currR][currC] == None:
                    queue.append((currR, currC, dis+1))
                    heights[currR][currC] = dis+1

        return heights    