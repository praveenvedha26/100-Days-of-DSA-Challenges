# Problem 1976: Number of Ways to Arrive at Destination
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        min_heap=[(0,0)]
        dist=[float('inf')]*n
        dist[0]=0

        ways=[0]*n
        ways[0]=1

        Mod=10**9+7

        while min_heap:
            ti,st = heapq.heappop(min_heap)

            if ti>dist[st]:
                continue

            for dest,time in adj[st]:
                if ti+time<dist[dest]:
                    dist[dest]=ti+time
                    ways[dest]=ways[st]
                    heapq.heappush(min_heap,(ti+time,dest))
                elif ti+time==dist[dest]:
                    ways[dest]=(ways[dest]+ways[st])%Mod
        return ways[n-1]


