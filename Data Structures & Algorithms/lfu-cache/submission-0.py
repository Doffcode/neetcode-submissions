class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # cache[key] = [value, frequency, timestamp]
        self.timestamp = 0
          
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.timestamp += 1
        self.cache[key][1] += 1
        self.cache[key][2] = self.timestamp
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap <=0: return 
        
        self.timestamp += 1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.timestamp
            return 
        
        if len(self.cache) >= self.cap:
            minf = float('inf')
            mints = float('inf')
            lfkey = None
            
            for k, (_,f, ts) in self.cache.items():
                if f < minf or (f == minf and ts < mints):
                    minf = f
                    mints = ts
                    lfkey = k
            if lfkey is not None:
                 del self.cache[lfkey]

        self.cache[key] = [value, 1, self.timestamp]
        print(self.cache.items())

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)