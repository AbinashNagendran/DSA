class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        left = 0 
        right = x

        while (right - left > 1):
            mid = (right + left) / 2
            check = mid * mid 
            if check > x: 
                right = mid
            elif check < x: 
                left = mid
            else:
                return mid
        return int(left)
        