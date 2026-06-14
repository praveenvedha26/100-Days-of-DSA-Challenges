# Problem 787: Cheapest Flights Within K Stops
# Difficulty: Medium
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        path=defaultdict(list)
        for s,d,p in flights:
            path[s].append((d,p))

        min_heap=[(0,src,0)]
        costs=defaultdict(lambda: defaultdict(lambda:float('inf')))
        costs[src][0]=0

        while min_heap:
            pr,sr,stop=heapq.heappop(min_heap)
            
            if sr==dst:
                return pr
            
            if stop<=k:
                for nei,price in path[sr]:
                    new_cost=pr+price
                    if new_cost<costs[nei][stop+1]:
                        costs[nei][stop+1]=new_cost
                        heapq.heappush(min_heap,(new_cost,nei,stop+1))
                        
        return -1
        