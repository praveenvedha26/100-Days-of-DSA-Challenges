# Problem 1091: Shortest Path in Binary Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        res=[]
        visited=set()

        Q=collections.deque()
        Q.append([0,0,0])
        if grid[0][0]!=0:
            return -1
            
        while Q:
            r,c,l=Q.popleft()
            if (r,c) in visited:
                continue
            visited.add((r,c))

            if r==R-1 and c==C-1 and grid[r][c]==0:
                res.append(l+1)

            directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

            for dr,dc in directions:
                nr,nc = r + dr , c + dc

                if nr in range(R) and nc in range(C) and grid[nr][nc]==0:
                    Q.append([nr,nc,l+1])

        return min(res) if res else -1