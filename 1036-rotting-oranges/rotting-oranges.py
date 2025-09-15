class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 0):
                return
            visit.add((r, c))
            q.append([r, c])
            grid[r][c] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
        time = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r+1,c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            time+=1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time if time > 0 else 0
        