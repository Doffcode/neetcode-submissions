class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pc = defaultdict(int)
        pc[0] = 1
        sum = 0
        count = 0
        for n in nums:
            sum+=n
            np = sum - k
            if np in pc:
                count+=pc[np]
            pc[sum]+=1
        return count