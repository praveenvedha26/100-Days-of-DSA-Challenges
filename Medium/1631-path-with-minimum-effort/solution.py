# Problem 1631: Path With Minimum Effort
# Difficulty: Medium
# Link: https://leetcode.com/problems/path-with-minimum-effort/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        min_heap = [(0, 0, 0)]
        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if (r, c) == (rows - 1, cols - 1):
                return effort

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols):
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(min_heap, (new_effort, nr, nc))

        return 0













