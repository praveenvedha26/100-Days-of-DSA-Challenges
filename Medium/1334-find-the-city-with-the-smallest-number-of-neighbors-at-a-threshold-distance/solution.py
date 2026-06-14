# Problem 1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=defaultdict(list)
        for i,j,k in edges:
            adj[i].append((j,k))
            adj[j].append((i,k))

        def dijikstras(src):
            min_heap=[(0,src)]
            visited=set()
            while min_heap:
                dist,source=heapq.heappop(min_heap)
                if source in visited:
                    continue
                visited.add(source)
                for dest,weigh in adj[source]:
                    if dist+weigh<=distanceThreshold:
                        heapq.heappush(min_heap,[dist+weigh,dest])
            return len(visited)-1
        
        res,min_count=-1,n
        for i in range(n):
            count=dijikstras(i)
            if count<=min_count:
                res,min_count=i,count
        return res
            