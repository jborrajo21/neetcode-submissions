# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def dfs(node):
            nonlocal best
            if not node: return 0
            l = 1 + dfs(node.left) if node.left else 0
            r = 1 + dfs(node.right) if node.right else 0
            best = max(best, l + r)
            return max(l, r)
        
        dfs(root)
        return best