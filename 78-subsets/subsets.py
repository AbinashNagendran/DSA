class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        subset = []
        def backtrack(index):
            if index == len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
            backtrack(index + 1)
        backtrack(0)
        return ans
        