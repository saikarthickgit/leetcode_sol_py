class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if m<n:
            return False
        c=Counter(s1)
        s=""
        
        for i in range(0,m-n+1):
            s=s2[i:i+n]
            if c==Counter(s):
                return True
                break
        return False
            
        