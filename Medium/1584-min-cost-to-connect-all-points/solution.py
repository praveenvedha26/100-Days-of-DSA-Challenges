# Problem 1584: Min Cost to Connect All Points
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        min_heap=[(0,0)]
        min_cost=0
        edges_used=0
        while edges_used<n:
            sum,src=heapq.heappop(min_heap)

            if src in visited:
                continue

            visited.add(src)
            min_cost+=sum
            edges_used+=1

            for next_point in range(n):
                if next_point not in visited:
                    dist = abs(points[src][0] - points[next_point][0]) + abs(points[src][1] - points[next_point][1])
                    heapq.heappush(min_heap, (dist, next_point))

        return min_cost