# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # i though they were gonna give index an input but anyway

        # fast and slow pointer technique

        slow = head
        fast = head

        # both point to the same node 

        while fast and fast.next:  # to see if null exists

            slow = slow.next
            fast = fast.next.next

            if slow == fast:   #if both nodes are the same
                return True

        return False
        