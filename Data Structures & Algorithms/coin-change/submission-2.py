class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change=[amount+1]*(amount+1)
        
        change[0]=0
        for c in range(1,amount+1):
            for coin in coins:
                if c-coin>=0:
                    change[c]=min(change[c],change[c-coin]+1)
        return change[amount] if change[amount] != amount+1 else -1
