"""
KEY INSIGHTS
DFS WITH ADDITIONAL PARAMETER

KEY SUGGESTIONS
RETURNS ARE USELESS
JUST CALL DFS WITHOUT RETURN
"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # we need to visit every node
        # we need to keep track of a max within that path.
        # we can try a dfs
        # the dfs will append to a global var
        # how to keep track of max? 
        # we can add an extra parameter

        valid = []

        def dfs(root , maxx):
            if root is None: 
                return []
            if root.val >= maxx:
                maxx = root.val
                valid.append(root.val)
            return dfs(root.left, maxx) + [root.val] + dfs(root.right, maxx)
        
        dfs(root, root.val)
        return len(valid)

