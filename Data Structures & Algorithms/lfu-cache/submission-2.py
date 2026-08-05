class listnode:
    def __init__ (self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
class ll:
    def __init__(self):
        self.left = listnode(-1,-1)
        self.right = listnode(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.size =0
    
    def length (self):
        return self.size
    
    def pushright (self,node):
        prev = self.right.prev 
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1
    
    def pop (self,node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev, node.next = None, None
        self.size -= 1
    
    def popleft (self):
        if self.length() == 0: return None
        node = self.left.next
        self.pop(node)
        return node    

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.km = {}
        self.fm = defaultdict(ll)
        self.lfcount = 0

    def counter(self,node):
        cnt = node.freq
        self.fm[cnt].pop(node)
        if cnt == self.lfcount and self.fm[cnt].length() == 0:
            self.lfcount += 1
        node.freq += 1
        self.fm[node.freq].pushright(node)
        
    def get(self, key: int) -> int:
        if key not in self.km: return -1
        node = self.km[key]
        self.counter(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if self.cap <= 0: return
        
        if key in self.km:
            node = self.km[key]
            node.val = value
            self.counter(node)
            return

        if len(self.km) == self.cap:
            node = self.fm[self.lfcount].popleft()
            self.km.pop(node.key)

        node = listnode(key,value)
        self.km[key] = node
        self.fm[1].pushright(node)
        self.lfcount = 1





