class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        add = defaultdict(int)
        rem = defaultdict(int)
        laststop = 0
        currpass = 0
        for i in range (len(trips)):
            p,s,e = trips[i]
            add[s] += p
            rem[e] += p
            laststop = max(laststop,e)
        for i in range (laststop):
            currpass += (add[i] - rem[i])
            if currpass > capacity:
                return False
        return True
        
        