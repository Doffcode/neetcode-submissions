"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # now just a copy node and its mappind
        if not head: return None
        cur = head
        hm = {}
        while cur:
            hm[cur] = Node(cur.val)
            cur = cur.next
        #now just point the randompointer to the corr nodes
        cur = head
        while cur:
            if cur.next: hm[cur].next = hm[cur.next]
            if cur.random: hm[cur].random = hm[cur.random]
            cur = cur.next  
        return hm[head]








