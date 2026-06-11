class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res =[]
        seen = {}
        for i,n in enumerate (nums):
            comp = target - n
            if comp in seen:
                res.append(seen[comp])
                res.append(i)
            else:
                seen[n] = i
        return res