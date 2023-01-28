class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N ,minH= len(grid),[[grid[0][0],0,0]]
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                neiR ,neiC= r+dr ,c+dc
                if neiC < 0 or neiR < 0 or neiR >=N or neiC>=N or grid[neiR][neiC]==-1:
                    continue
                heapq.heappush(minH, [ max(t,grid[neiR][neiC]), neiR,neiC])
                grid[neiR][neiC]=-1