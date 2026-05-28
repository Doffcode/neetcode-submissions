class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted (nums)
        ret = []
        cset = set()
        for i in range (len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                 continue
            target = -nums[i]
            seen = set()

            for j in range (i,len(nums)) :
                if (j!=i):
                    num = nums[j]
                    comp = target - nums[j]
                    if comp in seen:
                        c = [nums[i], num, comp]
                        c = sorted(c)
                        if tuple(c) not in cset:
                            ret.append(c)
                            cset.add(tuple(c))
                    else:
                        seen.add(num)
        return ret