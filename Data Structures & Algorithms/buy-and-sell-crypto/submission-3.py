class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0
        min_price=prices[0]
        # buy=0

        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
                # buy=i
            profit=prices[i]-min_price
            max_profit=max(profit,max_profit)
        return max_profit