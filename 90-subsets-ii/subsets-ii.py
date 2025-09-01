class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        
        def dfs(index, subset):
            if index == len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
            while(index + 1 < len(nums) and nums[index] == nums[index + 1]):
                index+=1
            dfs(index + 1, subset)
        dfs(0, [])
        return ans
        