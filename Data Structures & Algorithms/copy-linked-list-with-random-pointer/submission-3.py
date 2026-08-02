class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur,hm = head,{}
        while cur:
            hm[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next: hm[cur].next = hm[cur.next]
            if cur.random: hm[cur].random = hm[cur.random]
            cur = cur.next  
        return hm[head]