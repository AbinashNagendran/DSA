class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = [None] * n
        def bruteforce(cur):
            if cur > n:
                return 0
            if cur == n: 
                return 1
            if memo[cur] != None: 
                return memo[cur]

            result =  bruteforce(cur + 1) + bruteforce(cur + 2)
            memo[cur] = result
            return result

        return bruteforce(0)
        