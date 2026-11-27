class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini=prices[0]
        temp=0
        for i in range(1,len(prices)):
            if prices[i]>mini:
                temp=max(prices[i]-mini,temp)
            else:
                mini=prices[i]
            
        return temp
        