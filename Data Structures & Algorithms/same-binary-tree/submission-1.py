"""
KEY INSIGHT:
return True only returns to the previous call, not the entire program
THE AND IN LAST RETURN WILL DO BOOLEAN ALGEBRA

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    # we have two requirements
    # same structure
    # same value in structure

        if p is None and q is None: return True
        if p is None and q is not None: return False
        if p is not None and q is None: return False
        if p.val != q.val: return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)       