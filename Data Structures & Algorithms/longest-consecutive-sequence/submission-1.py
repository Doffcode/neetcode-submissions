class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for n in nums:
            if n-1 in numset:
                continue
            else:
                length = 0
                while(n+length in numset):
                    length += 1
                maxlen = max(length,maxlen)
        return maxlen

