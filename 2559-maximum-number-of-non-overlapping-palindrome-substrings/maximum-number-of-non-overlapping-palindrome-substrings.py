
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        l = 0

        def check_palindrome(temp: str) -> bool:
            return temp == temp[::-1]

        while l <= n - k:
            # 1. Check minimal substring of length k
            if check_palindrome(s[l : l + k]):
                count += 1
                l += k  # Jump past this palindrome to prevent overlap
            # 2. Check minimal substring of length k + 1
            elif l + k + 1 <= n and check_palindrome(s[l : l + k + 1]):
                count += 1
                l += k + 1  # Jump past this palindrome to prevent overlap
            else:
                l += 1  # Slide forward by 1 if no palindrome starts at l

        return count


'''class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s) #9-3
        count=0
        i=0
        l,j=0,0
        temp=""

        def check_palindrome(temp):
            return temp==temp[::-1] 

        while l<(n-k):
            temp=s[l:l+k]
            if(check_palindrome(temp)):
                count+=1
                j=j+1
            else:
                l+=1
                j=0
        return count'''




        