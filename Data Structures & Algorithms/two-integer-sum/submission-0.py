class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ret = []
        for i in range (len(nums)):
            comp =  target - nums[i]
            if comp in map :
                ret.append(map[comp])
                ret.append(i)
                return ret
            else:
                map[nums[i]] = i
        return ret