# Problem 542: 01 Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/01-matrix/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return mat
        r=len(mat)
        c=len(mat[0])
        distance=[[float('inf')for _ in range(c)]for _ in range(r)]
        Q=collections.deque()

        for row in range(r):
            for col in range(c):
                if mat[row][col]==0:
                    distance[row][col]=0
                    Q.append((row,col))

        while Q:
            x,y=Q.popleft()
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr,nc=x+dr,y+dc
                if nr in range(r) and nc in range(c):
                    if distance[nr][nc]>distance[x][y] +1:
                        distance[nr][nc]=distance[x][y] + 1
                        Q.append((nr,nc))
        return distance
