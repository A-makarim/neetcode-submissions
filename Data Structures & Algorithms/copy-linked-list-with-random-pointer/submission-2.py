"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # becaus we need to next to future nodes, we will do two pass

        current = head


# can't do this below
        #while current:
        #    new_node = Node(current.val, current.next, None)
        #    current = current.next

        old = {}
        while current:
            new_node = Node(current.val)
            old[current] = new_node   #current is the key, new node is the vlaue
            current = current.next

        print(old)

        current = head
            

        while current:
            copy = old[current]     #copy is the new node
            copy.next = old[current.next] if current.next else None   
            # think of it like like,
            # old[current.next] is a new key now, and it gives a new value, which is another new node
            copy.random = old[current.random] if current.random else None
            current = current.next

        return old[head] if head else None
            


        
            

        