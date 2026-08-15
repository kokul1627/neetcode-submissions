class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp=[amount+1]*(amount+1)
        dp[0]=0

        for amount in range(1,amount+1):
            for coin in coins:
                if amount-coin>=0:
                    dp[amount]=min(dp[amount],dp[amount-coin]+1)
        return dp[amount] if dp[amount]<amount+1 else -1



        # def dfs(amount):
        #     if amount == 0:
        #         return 0

        #     res = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     return res

        # minCoins = dfs(amount)
        # return -1 if minCoins >= 1e9 else minCoins