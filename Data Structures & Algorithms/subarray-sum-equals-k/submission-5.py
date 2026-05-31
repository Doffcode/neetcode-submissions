class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        prefix[0] = 1
        count = 0
        pref = 0
        sum =0
        for i in range (len(nums)):
            sum += nums[i]
            pref = sum - k
            if pref in prefix:
                count += prefix[pref]
            if sum in prefix:
                prefix[sum]+=1
            else:
                prefix[sum] = 1
        return count


