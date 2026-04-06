"""
KEY INSIGHTS
THE LCA WILL BE WHICHEVER NODE HAS A VALUE IN BETWEEN
THIS IS KEY IDEA OF BT
RETURN THE NODE WHEN YOU COME ACROSS THIS CONDITION
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # i can try a recursive funtion that goes to nodes based on bigger or smaller.
        # whenever there's a contrast, I can return (hopfeully. Let's try)
        if p.val> q.val:
            t = p
            p = q
            q =t
        if root.val >= p.val and root.val <= q.val: return root # let this be base case
        else: 
            if root.val < p.val: return self.lowestCommonAncestor(root.right , p , q) 
            else:
                return self.lowestCommonAncestor(root.left , p , q) 
