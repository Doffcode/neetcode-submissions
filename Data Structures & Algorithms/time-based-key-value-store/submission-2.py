class TimeMap:

    def __init__(self):
        self.kvs = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvs[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        vals = self.kvs[key]
        res = ""
        if key not in self.kvs:
            return res
        else:
            l,r = 0, len(vals)-1
            while l <= r:
                m = (l+r)//2
                if self.kvs[key][m][1] == timestamp:
                    return self.kvs[key][m][0]
                elif self.kvs[key][m][1] < timestamp:
                    res = self.kvs[key][m][0]
                    l = m+1
                else: r = m-1 
        return res