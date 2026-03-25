from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        if total%2 != 0:
            return False
        
        target = total//2
        m,n=len(grid),len(grid[0])

        prefix = 0
        for i in range(m):
            prefix+=sum(grid[i])

            if prefix == target and i<m-1:
                return True

        prefix = 0
        for j in range(n):
            prefix+=sum(grid[i][j] for i in range(m))

            if prefix == target and j<n-1:
                return True

        return False

        