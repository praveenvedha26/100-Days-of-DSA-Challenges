# Problem 947: Most Stones Removed with Same Row or Column
# Difficulty: Medium
# Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph={i: [] for i in range(len(stones))}
        for i,x in enumerate(stones):
            for j in range(i):
                y=stones[j]

                if x[0]==y[0] or x[1]==y[1]:
                    
                    graph[i].append(j)
                    
                    graph[j].append(i)
        visit=set()
        ans=0
        for i in range(len(stones)):
            if i not in visit:
                stack=[i]
                visit.add(i)

                while stack:
                    node=stack.pop()
                    for nei in graph.get(node, []):
                        if nei not in visit:
                            stack.append(nei)
                            visit.add(nei)
                            ans+=1
        return ans
