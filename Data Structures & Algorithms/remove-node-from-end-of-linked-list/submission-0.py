# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # n is given
        # what make sthis problem intersting is n starst countring from end

        # first instincts: reverse the list. but that's overkill, i think 
        # only way to remove it it to have known lenght of the list. subtract n from lenght. lets say this is m
        # then remove mth node
        # we can check lenght with fast and slow node

        # another way is to move the n steps ahead.
        # then move fast from nth and slow from head. 
        # the diff between them is constant of n. 

        # to make sure we don't lose our head, make a dummy

        dummy = ListNode(0, None)
        dummy.next = head

        slow = dummy
        fast = dummy

        # move fast until n
        for i in range(n):
            fast = fast.next

        # .next n times

        while fast.next: 
            slow = slow.next
            fast = fast.next 

        # the gap is constant

        # now that fast is at null and slow at n

        slow.next = slow.next.next

        # skipping one node

        return dummy.next





        