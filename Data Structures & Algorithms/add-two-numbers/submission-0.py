# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # edgecase1: not same length
        # edgecase2: carry

        # first head: L1
        # second head: L2
        out = ListNode()
        current = out

        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            print(num1, num2)





            summ = num1 + num2 + carry 


            carry = summ//10
            left = summ % 10
            

            temp = ListNode(left)
            current.next = temp

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            current = current.next

        return out.next










        
        