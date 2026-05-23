class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numset:
                lenght = 0
                while ((n+lenght) in numset):
                    lenght +=1
                longest = max (longest ,lenght)
        return longest

        