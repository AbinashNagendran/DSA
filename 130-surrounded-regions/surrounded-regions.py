class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        def dfs(i,j):
            if (i < 0 or j < 0 or i == ROW or j == COL or board[i][j] != "O"):
                return 
            board[i][j] = "#"

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j) 
            dfs(i, j - 1)
            
        # top and bottom border
        for j in range(COL):
            if board[0][j] == "O":
                dfs(0,j)
            if board[ROW - 1][j] == "O":
                dfs(ROW - 1, j)

        for i in range(ROW):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][COL - 1] == "O":
                dfs(i, COL - 1)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
        