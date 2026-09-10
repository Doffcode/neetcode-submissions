class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        maxfreq = max(freq.values())
        c = 0
        for fval in freq.values():
            if fval == maxfreq:c+=1
        noue = len(freq)

        if n >= noue:
            return (n+1) * (maxfreq-1) + c
        else: return len(tasks)