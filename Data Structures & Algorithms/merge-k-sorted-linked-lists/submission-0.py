# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        length = len(lists)
        dummy = ListNode()
        curr = dummy

        if lists is None:
            return dummy.next

        while True: # some condition to check all list are null:
            minimum = float('inf')
            smallest = -1

            for i in range(length):
                if lists[i] is not None:
                    temp = lists[i].val
                    if temp < minimum:
                        minimum = lists[i].val       # we know which head will haev minimum
                        smallest = i
            if smallest == -1:
                return dummy.next
            
            temp2 = lists[smallest].next
            curr.next = lists[smallest]          # head of smallest list 
            lists[smallest] = temp2


            curr = curr.next







            
        