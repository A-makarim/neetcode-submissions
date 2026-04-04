# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_head = None
        prev_tail = None
        while True:
            # i need to track prev tail, and head of new
            if self.has_k(head, k): # yes or no
                if prev_tail is None:
                    head, prev , save = self.flip_k(head, k)  # prev is head of new. save is tail of new
                    prev_tail = save  # save is first node, tail. head to be 
                    prev_head = prev
                else:
                    head, prev , save = self.flip_k(head, k)  # prev is head of new. save is tail of new
                    prev_tail.next = prev  # save is frist node, head to be 
                prev_tail = save



                

            else:
                break
        try:
            print("prev")
            return prev_head
        except:
            return head 
        # we need a function to check if next k nodes exist: this function will return true or false
    def has_k(self, head, k):
        save_head = head
        for i in range(k):
            if save_head is None:
                return False
            save_head = save_head.next
        head = save_head   # head repositions
        return True

    def flip_k(self, head, k):
        prev = None
        save = head # head of processed chunk to be 

        for i in range(k):                
            forward = head.next
            head.next = prev
            prev = head
            head = forward

        save.next = forward # joined to forward
        #self.connector(prev, save)

        
        return  head, prev, save  # forward is 3 

    def connector(self, prev, head):  # prev of processed chucnk and head of prev chunk
        head.next = prev

        
        