# Problem 130: Surrounded Regions
# Difficulty: Medium
# Link: https://leetcode.com/problems/surrounded-regions/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Row,Col=len(board),len(board[0])
        def capture(r,c):
            if r<0 or c<0 or r==Row or c==Col or board[r][c]!="O":
                return
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for r in range(Row):
            for c in range(Col):
                if (r in [0,Row-1] or c in [0,Col-1]) and board[r][c]=="O":
                    capture(r,c)

        for r in range(Row):
            for c in range(Col):
                if board[r][c]=="O":
                    board[r][c]="X"

        for r in range(Row):
            for c in range(Col):
                if board[r][c]=="T":
                    board[r][c]="O"

        
        