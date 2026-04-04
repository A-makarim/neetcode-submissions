# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          # head is a node

        prev = None   # no prev note
        current = head

        while current:
            n = current.next    # save the next link first
            current.next = prev     # point it to prev node instead
            prev = current    # prev pointed 
            current = n     

        return prev


# Reverse: 1 -> 2 -> 3 -> None
#
# Start:
# 1 -> 2 -> 3 -> None
#
# Step 1:
# 1 <- 2 -> 3 -> None
#
# Step 2:
# 1 <- 2 <- 3 -> None
#
# Step 3:
# 1 <- 2 <- 3
#
# Read backwards:
# 3 -> 2 -> 1 -> None
