class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # rows = len(matrix)
        # cols = len(matrix[0])

        # for i in range(0,rows):


            
        #     if target > matrix[i][cols-1]:
        #         i+=1 

        #     elif target >= matrix[i][0] and target <= matrix[i][cols-1]:
        #         for j in range(0, cols):
        #             if target == matrix[i][j]:
        #                 return True

        # return False

        rows = len(matrix)
        cols = len(matrix[0])

        top, bot = 0, rows - 1

        while top <= bot:
            row = (top+bot)//2

            if target > matrix[row][-1]:
                top  = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not(top<=bot):
            return False
        
        row = (top+bot)//2
        l, r =0 , cols-1

        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False 



        