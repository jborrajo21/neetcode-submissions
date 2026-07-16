# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            traversal.append(node.val)
            if node.right:
                traverse(node.right)

        traverse(root)
        return traversal[k - 1] 