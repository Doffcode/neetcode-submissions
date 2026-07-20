class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.maxcnt = 0
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        valcnt = self.cnt[val]
        self.maxcnt = max(valcnt,self.maxcnt)
        self.stacks[valcnt].append(val) 
    
    def pop(self) -> int:
        res = self.stacks[self.maxcnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxcnt]:
            self.maxcnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()