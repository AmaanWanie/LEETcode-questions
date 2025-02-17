class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            col = list()
            for j in range(len(grid)):
                col.append(grid[j][i])

            for row in grid:
                if row == col:
                    count+=1
        return count
                
