class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = (len(nums) -k) % len(nums)
        nums1 = nums[k:]+nums[:k]
        nums[:] = nums1
        