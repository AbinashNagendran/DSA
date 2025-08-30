class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while(len(stones) > 1):
            max1 = -heapq.heappop(stones)
            max2 = -heapq.heappop(stones)
            if max1 == max2:
                continue
            else:
                # max2 destroyed
                res = max1 - max2
                heapq.heappush(stones, -res)
        
        return -stones[0] if stones else 0 
        