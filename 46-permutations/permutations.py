class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(subset, chosen):
            if len(subset) == len(nums):
                ans.append(subset[:])

            for i in range(len(nums)):
                if not chosen[i]:
                    chosen[i] = True
                    subset.append(nums[i])
                    dfs(subset, chosen)
                    subset.pop()
                    chosen[i] = False

            
        chosen = []
        for i in range(len(nums)):
            chosen.append(False)
        dfs([], chosen)
        return ans
        