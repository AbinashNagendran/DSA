class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        candidates.sort()

        def dfs(sol, i, total):
            if total == target:
                ans.append(sol[:])
                return
            if i >= len(candidates) or total > target:
                return

            sol.append(candidates[i])
            dfs(sol, i + 1, total + candidates[i])
            sol.pop()
            dup = candidates[i]
            while(i + 1 < len(candidates) and candidates[i] == candidates[i + 1]):
                i+=1
            dfs(sol, i + 1, total)
        dfs([], 0, 0)
        return ans