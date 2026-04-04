# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # use max depth but include left max and right max both

        self.diam = 0
        
        def dfs(root):
            if root == None:
                return 0
            self.diam = max(self.diam, dfs(root.left) + dfs(root.right))
            return 1 + max(dfs(root.left), dfs(root.right))

        dfs(root)
        return self.diam
        