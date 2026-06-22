# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h1 = h2 = ListNode()
        h1.next = h2.next = head
        dummy = h1
        for i in range (n+1):
            h1 = h1.next
        while h1:
            h1=h1.next
            h2=h2.next
        h2.next = h2.next.next
        return dummy.next

        