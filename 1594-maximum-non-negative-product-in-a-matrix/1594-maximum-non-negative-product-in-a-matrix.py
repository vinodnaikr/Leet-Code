class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
       
        dpMax = [[0] * n for _ in range(m)]
        dpMin = [[0] * n for _ in range(m)]
        
        
        dpMax[0][0] = dpMin[0][0] = grid[0][0]
        
       
        for j in range(1, n):
            dpMax[0][j] = dpMin[0][j] = dpMax[0][j-1] * grid[0][j]
        
       
        for i in range(1, m):
            dpMax[i][0] = dpMin[i][0] = dpMax[i-1][0] * grid[i][0]
        
       
        for i in range(1, m):
            for j in range(1, n):
                curr = grid[i][j]
                
               
                candidates = [
                    dpMax[i-1][j] * curr,
                    dpMin[i-1][j] * curr,
                    dpMax[i][j-1] * curr,
                    dpMin[i][j-1] * curr
                ]
                
                dpMax[i][j] = max(candidates)
                dpMin[i][j] = min(candidates)
        
        result = dpMax[m-1][n-1]
        
        return result % MOD if result >= 0 else -1