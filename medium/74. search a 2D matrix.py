# 74. search a 2D matrix
#time complexity O(log m * n) 


        ix = 0
        jx = len(matrix)-1

        while (ix<=jx):
            mid_row = (ix + jx)//2
            
            if target > matrix[mid_row][-1]:
                ix = mid_row + 1
            elif target < matrix[mid_row][0]:
                jx = mid_row - 1
            else :
                break

        ROW = mid_row

        iy = 0 
        jy = len(matrix[ROW])-1

        while (iy <= jy):
            mid_col = (iy + jy)//2
            
            if target == matrix[ROW][mid_col]:
                return True
            elif target > matrix[ROW][mid_col]:
                iy = mid_col + 1
            elif target < matrix[ROW][mid_col]:
                jy = mid_col - 1
            else :
                break
        return False
