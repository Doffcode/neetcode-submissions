class Solution:
    def climbStairs(self, n: int) -> int:
        if n== 1 :return 1
        if n== 2 :return 2
        a = 1
        b = 2
        ret = 0
        for i in range(2,n):
            sum = a+b
            a = b
            b = sum
        return sum

