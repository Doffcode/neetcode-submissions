class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        si = 0
        for i, n in enumerate(nums):
            if n != val:
                nums[si],nums[i] = nums[i],nums[si]
                si+=1
            else:
                continue
        return si