# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        good = 0


        def dfs(node, maximum):
            nonlocal good
            if node.val >= maximum:
                good += 1
                maximum = node.val
            if node.left:
                dfs(node.left, maximum)
            if node.right:
                dfs(node.right, maximum)
        
        dfs(root, root.val)
        return good
