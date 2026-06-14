# Problem 1020: Number of Enclaves
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-enclaves/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        corners=collections.deque()
        for Row in range(r):
            for Col in range(c):
                if (Row in [0,r-1] or Col in [0,c-1]) and grid[Row][Col]==1:
                    corners.append([Row,Col])
                    grid[Row][Col]=-1
        
        while corners:
            R,C=corners.popleft()
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr,nc=dr+R,dc+C
                if nr in range(r) and nc in range(c) and grid[nr][nc]==1:
                    corners.append((nr,nc))
                    grid[nr][nc]=-1
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    count+=1
        return count


        

        