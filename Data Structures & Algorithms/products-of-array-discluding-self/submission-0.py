class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        prod_nz = 1
        ret = [0]*(len(nums))
        for i in range (len(nums)):
            prod *= nums[i]
            if (nums[i] == 0):
                count +=1
            else :
                prod_nz *= nums[i]
        if (count <2):
            for i in range (len(nums)):
                if (nums[i]!=0):
                    ret[i] = int (prod/nums[i])
                else:
                    ret[i] = prod_nz
            return ret 
        return ret