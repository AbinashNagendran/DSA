class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        max_rate = piles[-1]
        while left <= right:
            index = int((left + right) / 2)
            counter = 0
            for num in piles:
                counter+=math.ceil(num/index)
            if counter > h:
                left = index + 1
            else:
                right = index - 1
                max_rate = index
        return max_rate
        