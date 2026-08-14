"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        nodes = {}
        def dfs(node, copy):
            nodes[node.val] = copy
            copy.val = node.val
            for n in node.neighbors:
                if n.val not in nodes:
                    dfs(n, Node())
            copy.neighbors = [nodes[n.val] for n in node.neighbors]
        
        head = Node()
        dfs(node, head)
        return head