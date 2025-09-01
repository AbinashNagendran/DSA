class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(sol, index, total):
            if total == target:
                ans.append(sol[:])
                return
            if index >= len(candidates) or total > target:
                return
            sol.append(candidates[index])
            dfs(sol, index, total + candidates[index])
            sol.pop()
            dfs(sol, index + 1, total)
            

        dfs([], 0, 0)
        return ans
        