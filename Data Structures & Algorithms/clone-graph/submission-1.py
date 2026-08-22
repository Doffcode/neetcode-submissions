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
        visited = set()
        while q:
            no = q.popleft()
            for n in no.neighbors:
                if n in clone: continue
                else:
                    q.append(n)
                    visited.add(n)
            nn = Node(no.val)
            clone[no] = nn

        q.append(node)
        traversed = set()
        while q:
            no = q.pop()
            if no not in traversed:
                for n in no.neighbors:
                    clone[no].neighbors.append(clone[n])
                    if n not in traversed:
                        q.append(n)
            traversed.add(no)
        return clone[node]