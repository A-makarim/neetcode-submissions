# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the second half of the list:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondhalf = slow.next
        slow.next = None   # we break the link. now we got two seperate lists
        prev = None

        # reverse the second half

        while secondhalf: 
            tmp = secondhalf.next
            secondhalf.next = prev
            prev = secondhalf
            secondhalf = tmp   

        # now merge
        first = head
        second = prev

        while second:
            tmp1 = first.next    # cuz link breaks
            tmp2 = second.next
            first.next = second    # step 1
            second.next= tmp1
            first = tmp1
            second = tmp2






        