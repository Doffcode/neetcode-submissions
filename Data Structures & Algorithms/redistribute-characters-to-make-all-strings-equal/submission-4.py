class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = 0
        l = len(words)
        seen = defaultdict(int)
        for n in words:
            count+=len(n)
            for c in n:
                seen[c]+=1
        if count % l !=0:
            return False
        for val in seen.values():
            if val % l != 0:
                return False
        return True 

