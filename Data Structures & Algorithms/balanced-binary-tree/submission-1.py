# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def dfs(root):
            nonlocal balanced
            if not root: return 0
            l,r = dfs(root.left), dfs(root.right)
            balanced = abs(l - r) <= 1 if balanced else False
            print(root.val, balanced, l, r)
            return 1 + max(l, r)

        '''
                1
            2       3
        4       5|      6
      7|              8|

      Trace:
      dfs(1)=4, dfs(2) = 3, dfs(4)=2, dfs(7) = 1,
      dfs(5) = 1, dfs(3)=3, dfs(6)=2, dfs(8) = 1
        '''
        
        dfs(root)
        return balanced