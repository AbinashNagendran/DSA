class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = 0

        for i in range(len(height)):
            product = min(height[left], height[right]) * (right - left)
            if product > maximum:
                maximum = product
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        
        return maximum 