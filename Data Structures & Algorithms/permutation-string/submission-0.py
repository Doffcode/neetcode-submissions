class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        key  = defaultdict(int)
        for s in s1:
            key[s] +=1
        val = defaultdict(int)
        for s in s2[:len(s1)]:
            val[s]+=1
        print (list(key))
        if val == key:
            return True
        for i in range (len(s2)-len(s1)):
            val[s2[i]]-=1
            if val[s2[i]] == 0:
                del val[s2[i]]
            val[s2[i+len(s1)]]+=1
            print (list(val))
            if val == key:
                return True
        return False