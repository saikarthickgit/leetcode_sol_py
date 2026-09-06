class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:return n-1
        ans=n//3
        rem=n%3
        if rem==1:
            return 3**(ans-1)*2*2
        if rem==2:
            return 3**(ans)*2
        return 3**ans