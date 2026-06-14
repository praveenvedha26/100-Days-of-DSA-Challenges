# Problem 785: Is Graph Bipartite?
# Difficulty: Medium
# Link: https://leetcode.com/problems/is-graph-bipartite/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors=[-1]*len(graph)

        for i in range(len(graph)):
            if colors[i]==-1:
                q=deque([i])
                colors[i]=0

                while q:
                    curnode=q.popleft()
                    curcolor=colors[curnode]

                    for neighbour in graph[curnode]:
                        if colors[neighbour]==-1:
                            colors[neighbour]=1-curcolor
                            q.append(neighbour)
                        if colors[neighbour]==curcolor:
                            return False
        return True

                    
        