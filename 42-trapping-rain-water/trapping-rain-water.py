class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        left = 0 
        right = len(height) - 1
        leftHighest = height[left]
        rightHighest = height[right]
        while left < right:
            if leftHighest < rightHighest:
                left+=1
                leftHighest = max(leftHighest, height[left])
                res+= leftHighest - height[left]
            else:
                right-=1
                rightHighest = max(rightHighest, height[right])
                res+= rightHighest - height[right]
        return res




        

   





        