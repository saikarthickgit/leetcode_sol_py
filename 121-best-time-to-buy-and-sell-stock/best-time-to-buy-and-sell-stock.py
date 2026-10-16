class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini=prices[0]
        maxi=0
        n=len(prices)
        for i in range(1,n):
            mini=min(mini,prices[i])
            maxi=max(maxi,prices[i]-mini)
        return maxi
        