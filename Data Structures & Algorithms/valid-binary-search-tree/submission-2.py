"""
KEY INSIGHTS
DFS WITH TWO MORE PARAMS
DONT JUST CHECK LOCAL CONDITIONS
<ROOT.VAL ON LEFT? FINE. BUT IS IT GREATER THAN ANY ANCESTOR?
KEEP CHANGING MAX AND MIN TO ACCOUNT FOR THIS 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # dfs with cheking consitions for root.left and root.right


        def dfs(root, minn, maxx):
            if root is None:
                return True
            if not (minn<root.val<maxx):
        
                return False
            return dfs(root.left, minn, root.val) and dfs(root.right, root.val, maxx)



        return dfs(root, float('-inf'), float('inf'))
