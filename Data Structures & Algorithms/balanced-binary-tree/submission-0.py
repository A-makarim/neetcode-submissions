# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

    # we need height at every node
    # see if left and right differ more than one
    # thought process: 
        # use diameter problem but do left - right <=1 instead of adding them 
        self.isbalanced = True

        def dfs(root):
            if root is None:
                return 0 
            balcheck = dfs(root.left) - dfs(root.right)
            if abs(balcheck) >= 2:
                self.isbalanced = False
            return 1 + max(dfs(root.left), dfs(root.right))  # this returns max depts from each node
        
        dfs(root)
        return self.isbalanced