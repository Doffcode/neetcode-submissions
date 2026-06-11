class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        si = 0
        for i,n in enumerate(nums):
            if n == val:
                continue
            nums[si] = n
            si += 1
        return si

        