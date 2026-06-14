# Problem 733: Flood Fill
# Difficulty: Easy
# Link: https://leetcode.com/problems/flood-fill/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r,c=len(image),len(image[0])
        startcolor=image[sr][sc]
        if startcolor ==color:
            return image

        def bfs(sr,sc):
            Q=collections.deque()
            
            Q.append((sr,sc))
            while Q:
                row,col=Q.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                image[row][col]=color
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if nr in range(r) and nc in range(c) and image[nr][nc]==startcolor:
                        Q.append((nr,nc))
                       
                        image[nr][nc]=color

        bfs(sr,sc)
        return image