"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # make a copy of the node
        # add neighbours. 
        # to add neighbours we need their copy too btw.
        # if it's already a copy, don't clone it again

        cc = {}
        def dfs(node):
            if node in cc: 
                return cc[node]
            copy = Node(node.val)
            # we have a node. no neighbours attached yet
            cc[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))  # need a return statement for the base case to add neighbours
            return copy
        return dfs(node) if node else None

            # if alr in copy, 


        