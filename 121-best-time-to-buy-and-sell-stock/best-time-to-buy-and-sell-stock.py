class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0 
        end = 1
        output = 0
        while end < len(prices):
            sum = prices[end] - prices[start]
            if sum > 0:
                if sum > output:
                    output = sum
                end+=1
            else:
                start+=1
                if start == end:
                    end+=1

        return output