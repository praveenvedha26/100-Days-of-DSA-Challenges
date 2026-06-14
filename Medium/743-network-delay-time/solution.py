# Problem 743: Network Delay Time
# Difficulty: Medium
# Link: https://leetcode.com/problems/network-delay-time/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited=defaultdict()
        edges=defaultdict(list)
        for start,end,time in times:
            edges[start].append([time,end])
        signals=[[0,k]]
        while signals:
            length,node=heappop(signals)
            if node in visited:
                continue
            visited[node]=length

            for time,end in edges[node]:
                if end not in visited:
                    heappush(signals,[length+time,end])
            if len(visited)==n:
                return max(visited.values())
        return -1