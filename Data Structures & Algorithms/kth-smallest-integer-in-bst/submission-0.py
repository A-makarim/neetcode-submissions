# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # My first though is to traverse thru every one of them and give asw
        # but i have an advantage. i can only just keep going left. but no, they if K is huge
        # thinking...
        # use DFS, and stop when K elements are returned
        var = []


        def dfs(root):
            if root is None:
                return

            if len(var) == k:
                return

            # if its not, we obv want it to continue
            dfs(root.left)

            if len(var) < k:
                var.append(root.val)

            dfs(root.right)

        
        dfs(root)
        print(var)


        return var[k-1]
        
        




