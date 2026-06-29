class Solution:
    def romanToInt(self, s: str) -> int:

        n=len(s)
        t={
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }

        result=0
        for i in range(n-1):
            if t[s[i]]<t[s[i+1]]:
                result-=t[s[i]]
            else:
                result+=t[s[i]]
        return result+t[s[-1]]
        