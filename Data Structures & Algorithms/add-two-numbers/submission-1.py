# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1,l2
        s1 = s2 = ""
        while h1:
            s1 += str(h1.val)
            h1=h1.next
        while h2:
            s2 += str(h2.val)
            h2 =h2.next
        sum  = int(s1[::-1]) + int(s2[::-1])
        sum = str(sum)[::-1]
        dummy = ListNode(0)
        head = dummy
        for c in sum:
            dummy.next = ListNode(int(c))
            dummy = dummy.next
        return head.next
