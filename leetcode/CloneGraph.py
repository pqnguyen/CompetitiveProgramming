# https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        m = {}
        cloneNode = self.dfs(node, m)
        return cloneNode

    def dfs(self, node, m):
        if not node: return None
        cloneNode = Node(node.val, [])
        m[node] = cloneNode
        for neighbor in node.neighbors:
            if neighbor not in m:
                self.dfs(neighbor, m)
        for neighbor in node.neighbors:
            cloneNode.neighbors.append(m[neighbor])
        return cloneNode
