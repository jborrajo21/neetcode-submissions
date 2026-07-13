# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot): return True
        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            if not self.isSameTree(p.left, q.left):
                return False
            if not self.isSameTree(p.right, q.right):
                return False
            return True
        elif not p and not q:
            return True
        return False