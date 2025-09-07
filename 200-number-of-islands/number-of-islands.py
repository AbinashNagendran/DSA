class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def countIsland(i, j):
            if not (i >= 0 and i < len(grid) and
                j >= 0 and j < len(grid[0]) and
                grid[i][j] == "1" and not (i, j) in seen):
                return 
            seen.add((i, j))
            countIsland(i + 1, j)
            countIsland(i - 1, j)
            countIsland(i, j  + 1)
            countIsland(i, j - 1)
            return

        seen = set() 
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i, j) in seen:
                    countIsland(i, j)
                    count+=1
        return count
        