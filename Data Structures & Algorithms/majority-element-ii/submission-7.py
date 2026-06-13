class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand = defaultdict(int)
        ret = []
        for n in nums:
            if n in cand:
                cand[n]+=1
            else:
                if len(cand) <= 1:
                    cand[n] = 1
                else:
                    for key in cand:
                        cand[key]-=1
            for key in list(cand.keys()):
                if cand[key] <= 0:
                    del cand[key]
        print (cand)
        for key in cand:
            if nums.count(key) > len(nums)//3:
                print (nums.count(key))
                ret.append(key)
        return ret
                    