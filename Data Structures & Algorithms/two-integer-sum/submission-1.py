class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ret = []
        for i in range (len(nums)):
            comp =  target - nums[i]
            if comp in map :
                return [map[comp],i]
            map[nums[i]]=i
        return ret