# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if root is None: 
                return "!#"
            return "!" + str(root.val) + dfs(root.left) + dfs(root.right)

        return dfs(root)
    

    def strtolist(self, string, separator):
        l = string.split(separator)
        return l[1:]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = self.strtolist(data, "!")

        count = -1
        def makedfs():
            nonlocal count; count += 1

            if l[count] == "#":
                return None

            root = TreeNode(int(l[count]))

            root.left = makedfs()
            root.right = makedfs()

            return root

        return makedfs()


    
