# Problem 133: Clone Graph
# Difficulty: Medium
# Link: https://leetcode.com/problems/clone-graph/
# Language: python3
# ────────────────────────────────────────

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def clone(self,node,visited):
        if node in visited:
            return visited[node]
        cloned_node=Node(node.val)
        visited[node]=cloned_node
        for neighbour in node.neighbors:
            cloned_node.neighbors.append(self.clone(neighbour,visited))
        return cloned_node
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visited={}
        return self.clone(node,visited)
        