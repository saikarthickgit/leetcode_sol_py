class Solution:
    def prodDigits(self, n:int) -> int:
        prod = 1
        while n>0:
            prod *= n%10
            n //= 10
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.prodDigits(n)%t == 0:
                return n
            else:
                n+=1