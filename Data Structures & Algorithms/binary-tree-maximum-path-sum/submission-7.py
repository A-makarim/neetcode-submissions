# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = -11111

        def dfs(root):
            if not root: 
                return 0
            a = dfs(root.left)
            b = dfs(root.right)
            maxx = max(root.val, root.val + a , root.val + b, 0)
            self.ans = max(self.ans, root.val + a + b)
            return maxx # goes to the parent
        dfs(root)
        return self.ans