class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        first = 1
        second = 1
        ans = zero + first + second
        if n==0 or n==1:
            return n
        if n == 2:
            return 1
        for i in range(n-3):
            zero = first
            first = second
            second = ans
            ans = zero + first + second
        return ans 