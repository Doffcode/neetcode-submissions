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
        #first ill just create a copy without random and also mapping it along the way
        if not head: return None
        hm = {}
        nhead = Node(head.val)
        hm[head] = nhead
        n1, n2 = nhead, head
        while n2.next:
            n1.next = Node(n2.next.val)
            hm[n2.next] = n1.next
            n1 = n1.next
            n2 = n2.next 
        #now just point the randompointer to the corr nodes
        n1, n2 = head, nhead
        while n1:
            if n1.random != None:
                n2.random = hm[n1.random]
            n1 = n1.next
            n2 = n2.next
        return nhead








