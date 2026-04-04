"""
KEY INSIGHTS
USE THE SAME LOGIC AS LAST COMMIT: DIAMETR OF BINARY TREE
INSTEAD OF STORING MAX OF EVERY NODE LIKE IN SELF.DIAM
JUST STORE A FALSE AT ANY NODE WHEREVER DFS LENGTH OF LEFT AND RIGHT DIFFER MORE THAN 1
"""

"""
KEY SUGGESTIONS
DON'T CALL DFS TWICE IN BALCHECK AND RETURN
JUST MAKE A VARIABLE AND CALL RETURN IT THERE ONCE

EXAMPLE: 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isbalanced = True

        def dfs(root):
            if root is None:
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)

            balcheck = left - right
            if abs(balcheck) >= 2:
                self.isbalanced = False
            
            return 1 + max(left, right)  # this returns max depth from each node
        
        dfs(root)
        return self.isbalanced
"""


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


