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
        #first ill just create a copy without randon
        def cpll(head) -> Node:
            if not head: return None
            nhead = Node(head.val)
            curn = nhead
            curo = head.next
            while curo:
                curn.next = Node(curo.val)
                curn.random = None
                curn = curn.next
                curo = curo.next
            return nhead
        nhead = cpll(head)
        #mapping the nodes in the oll to the new ll
        mapping = {}
        th1,th2 = head,nhead
        while th1:
            mapping[th1] = th2
            th1 = th1.next
            th2 = th2.next

        
        #now just point the randompointer to the corr nodes
        n1, n2 = head, nhead
        while n1:
            if n1.random != None:
                n2.random = mapping[n1.random]
            n1 = n1.next
            n2 = n2.next
        return nhead








