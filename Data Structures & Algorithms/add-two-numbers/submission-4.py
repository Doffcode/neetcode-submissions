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
        while h1 or h2:
            if h1:
                val1 = h1.val
            else:
                val1 = 0
            if h2:
                val2 = h2.val
            else:
                val2 = 0
            csum = (val1+val2+carry)%10
            carry = (val1+val2+carry)//10
            h3.next = ListNode(csum)
            if h1:
                h1 =h1.next
            if h2:
                h2 = h2.next
            h3 = h3.next
        if carry !=0:
            h3.next = ListNode(carry)
        return l3.next
