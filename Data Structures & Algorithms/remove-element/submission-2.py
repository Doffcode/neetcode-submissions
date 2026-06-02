class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        si = 0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[i],nums[si] = nums[si], nums[i]
                si+=1
        return si

        