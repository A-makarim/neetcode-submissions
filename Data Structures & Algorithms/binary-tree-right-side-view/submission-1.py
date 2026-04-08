"""
KEY INSGIHTS
USE BFS FOR GETTING LEVEL ORDER SUBLISTS
JUST RETURN THE RIGHT MOST
"""


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for every layer, return rightmost
        # dicard left? no. go left,
        # return val if mroe depth

        # first idea: use BFS, return last of every sub list. 
        ans = []
        def bfs(root):
            if root is None: return []
            q = deque([root])

            while q:
                level = []
                for i in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)

                ans.append(level)

        bfs(root)
        final = []
        print(ans)
        # now i need last of every sublist"
        # edit: not last. FIRST
        for i in ans:
            final.append(i[0])

        return final
                        
            
        