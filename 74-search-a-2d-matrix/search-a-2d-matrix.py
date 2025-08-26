class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on first column then binary search hori on that 

        left = 0 
        right = len(matrix) - 1
        while left <= right:
            indexR = (left + right) // 2
            num = matrix[indexR][0]
            if num == target:
                return True
            if target > num:
                if target > matrix[indexR][-1]:
                    left = indexR + 1
                else:
                    break
            else: 
                right = indexR - 1

        left = 0 
        right = len(matrix[indexR]) - 1
        while left <= right:
            indexC = (left + right) // 2
            num = matrix[indexR][indexC]
            if num == target:
                return True
            elif num > target:
                right = indexC - 1
            else:
                left = indexC + 1
        return False
        


        