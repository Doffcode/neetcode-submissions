class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        for i in range (len(nums)-2):
            map = {}
            target = -nums[i]
            for j in range (i+1,len(nums)):
                comp = target - nums[j]
                if comp in map:
                    temp = [nums[i],nums[j],comp]
                    ret.add(tuple(sorted(temp)))
                else:
                    map[nums[j]] = (nums[j],j)
        return list(ret)