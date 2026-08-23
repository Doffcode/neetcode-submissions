"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return 
        clone = {}
        q = deque()
        q.append(node)
        clone[node] = Node(node.val)
        while q:
            no = q.popleft()
            for n in no.neighbors:
                if n not in clone:
                    q.append(n)
                    clone[n] = Node(n.val)  
                clone[no].neighbors.append(clone[n])
        return clone[node]