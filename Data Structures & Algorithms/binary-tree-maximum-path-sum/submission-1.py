# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = -11111

        def dfs(root): # each node will be review once from bottom up. using preorder
            # base case
            if not root: 
                # we should return zero
                return float('-inf')
            
            # take max
            a = dfs(root.left)
            b = dfs(root.right)
            total = a + b + root.val
            self.ans = max(total, a , b, root.val, self.ans)
            print(root.val)
            print("ans",self.ans)
            maxx = max(root.val, a, b)

            return maxx
        
        dfs(root)

        return self.ans
