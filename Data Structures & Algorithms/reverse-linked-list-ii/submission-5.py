
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for _ in range(left):
            leftnode = curr
            curr = curr.next
        rightnode = curr
        prev = None
        for i in range(right-left+1):
            if curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        leftnode.next = prev
        rightnode.next = curr
        return dummy.next
