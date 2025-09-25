class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 2 pointers for selling and buying
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0: 
                if profit > max_profit:
                    max_profit = profit
                r+=1 
            else:
                l+=1 
                if l == r:
                    r+=1
        
        return max_profit




        