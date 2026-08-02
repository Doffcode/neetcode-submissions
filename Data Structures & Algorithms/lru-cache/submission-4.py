class listnode:
    def __init__(self,key,val,prev,next):
        self.key, self.val, self.prev, self.next = key, val, prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = listnode(0,0,None,None)
        self.right = listnode(0,0,self.left,None)
        self.left.next = self.right    
        self.hm = {}

    def get(self, key: int) -> int:
        ret = -1
        if self.left.next == self.right: return -1
        if key in self.hm:
            node = self.hm[key]
            ret = node.val
            node.prev.next, node.next.prev = node.next, node.prev
            node.next, node.prev = self.right, self.right.prev
            self.right.prev.next, self.right.prev = node,node 
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            n = self.hm[key]
            n.prev.next, n.next.prev = n.next, n.prev
            node = listnode(key,value,self.right.prev,self.right)
            self.right.prev.next, self.right.prev = node, node
            self.hm[key] = node
        else:
            node = listnode(key,value,self.right.prev,self.right)
            self.right.prev.next, self.right.prev = node, node
            self.hm[key] = node
            if self.cap == 0:    
                del self.hm[self.left.next.key]
                node = self.left.next
                self.left.next = node.next
                node.next.prev = self.left
            else: self.cap -= 1  