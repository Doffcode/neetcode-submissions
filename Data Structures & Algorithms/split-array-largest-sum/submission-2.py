class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)
        ret = r
        def validsplit(largest) -> bool:
            split = 0
            csum = 0
            for n in nums:
                csum += n
                if csum > largest:
                    split+=1
                    csum = n
            if split + 1 <= k:
                return True
            else:
                return False
        if k == len(nums): return l
        elif k == 1: return r
        else:
            while l<=r:
                m = l + (r-l)//2
                if validsplit(m):
                    ret = m
                    r = m-1
                else:
                    l = m+1
        return ret

