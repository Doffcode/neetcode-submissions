# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def revll(self,s) -> ListNode:
        prev = None
        cur = s
        while cur :
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum = ListNode(0)
        dum.next = head
        pll = dum
        s, e = head, head
        f = True
        while True:
            for i in range (k-1):
                if e:
                    e = e.next
                else:
                    break
            if e:
                nll = e.next
                e.next = None
                pll.next = self.revll(s)
                s.next = nll
                pll = s
                s = e = nll
            else:
                break
        return dum.next












