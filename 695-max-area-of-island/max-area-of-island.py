class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 0  # mark visited
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) +  dfs(i, j + 1) + dfs(i, j - 1)

        biggest = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    biggest = max(dfs(i, j), biggest)
                    
        return biggest