# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1,l2
        l3 = ListNode(0)
        h3 = l3
        carry = 0
        while h1 and h2:
            csum = (h1.val+h2.val+carry)%10
            carry = (h1.val+h2.val+carry)//10
            h3.next = ListNode(csum)
            h1,h2,h3 = h1.next,h2.next,h3.next
        while h1:
            csum =  (h1.val+carry)%10
            carry = (h1.val+carry)//10
            h3.next = ListNode(csum)
            h1,h3 = h1.next,h3.next
        while h2:
            csum =  (h2.val+carry)%10
            carry = (h2.val+carry)//10
            h3.next = ListNode(csum)
            h2,h3 = h2.next,h3.next
        else:
            if carry != 0:
                h3.next = ListNode(carry)
        return l3.next
