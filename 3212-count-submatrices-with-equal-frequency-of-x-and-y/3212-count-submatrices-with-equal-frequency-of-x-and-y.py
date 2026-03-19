class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0

        countX=[0]*cols
        countY=[0]*cols

        for r in range(rows):
            row_x=0
            row_y=0

            for c in range(cols):
                
                if grid[r][c]=='X':
                    row_x+=1
                elif grid[r][c]=='Y':
                    row_y+=1
                
                countX[c]+=row_x
                countY[c]+=row_y

                if countX[c]==countY[c] and countX[c]>0:
                    count+=1
        
        return count