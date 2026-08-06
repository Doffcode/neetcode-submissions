# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def ml(self,h1,h2) -> ListNode:
        dummy = ListNode(0)
        h3 = dummy
        while h1 and h2:
            if h1.val <= h2.val: 
                dummy.next = h1
                h1 = h1.next
            else:
                dummy.next = h2
                h2 = h2.next
            dummy = dummy.next
        dummy.next = h1 if h1 else h2
        return h3.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        st = deque()
        st.append(ListNode(-float('inf')))
        for n in lists: st.append(n)
        while len(st)>1:
            n1 = st.popleft()
            n2 = st.popleft()
            st.append(self.ml(n1,n2))
        return st[0].next