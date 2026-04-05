# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        "if you reach value that is equal to sub tree root.val, start doing same binary tree prolem"
        "if you reach a root.val again, run another check"

        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    # we have two requirements
    # same structure
    # same value in structure

            if p is None and q is None: return True
            if p is None and q is not None: return False
            if p is not None and q is None: return False
            if p.val != q.val: return False
            return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

        if subRoot is None: return True
        
        if root is None: return False
        if root.val == subRoot.val:
            # return isSameTree(root, subRoot) this wont work cuz we need another recursive call. subtree might be at another root.val
            if isSameTree(root, subRoot):
                return True # if False, the next line does the recursive call to handle the case above
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
               
        
        