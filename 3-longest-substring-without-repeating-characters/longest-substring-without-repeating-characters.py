class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=""
        n=len(s)
        if n==0:
            return 0
        maxi=0


        for i in range(0,n):
            while s[i] in a:
                a=a[1:]
            a+=s[i]
            maxi=max(maxi,len(a))
           
        return maxi
        


        