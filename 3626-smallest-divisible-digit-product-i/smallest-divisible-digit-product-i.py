class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def repeat_it(n):
            sum=1
            while n>0:
                sum*=n%10
                n=n//10
            return sum

        while repeat_it(n)%t!=0:
            n+=1
        return n

        