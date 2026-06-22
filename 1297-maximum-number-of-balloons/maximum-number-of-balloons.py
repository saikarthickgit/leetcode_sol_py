class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mini=10000001
        mini1=10000001
        c=Counter(text)
        for ch in "balon":
            if ch=="l" or ch=="o":
                mini=min(c[ch]//2,mini)
            else:
                mini1=min(c[ch],mini1)
        return min(mini,mini1)
     
        