class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCoins = [0]*(amount+1)
        
        #recursionm
        
        for a in range(1, amount+1):
            minCoins[a]= 1+ min((float('inf') if a-coinVal <0 else minCoins[a-coinVal]) for coinVal in coins)
        
        # convert to leetcode's -1:
        if minCoins[amount] == float('inf'):
            return -1
        return minCoins[amount]
        