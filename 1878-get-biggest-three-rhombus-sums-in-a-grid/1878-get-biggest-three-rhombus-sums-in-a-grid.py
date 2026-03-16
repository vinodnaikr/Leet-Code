class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
               
                sums.add(grid[r][c])
                
                
                k = 1
                while True:
                    
                    if r - k < 0 or r + k >= m or c - k < 0 or c + k >= n:
                        break
                    
                    curr_sum = 0
                   
                    
                    for i in range(k):
                        curr_sum += grid[r - k + i][c + i]
                    
                    for i in range(k):
                        curr_sum += grid[r + i][c + k - i]
                    
                    for i in range(k):
                        curr_sum += grid[r + k - i][c - i]
                   
                    for i in range(k):
                        curr_sum += grid[r - i][c - k + i]
                    
                    sums.add(curr_sum)
                    k += 1
        
        
        return sorted(list(sums), reverse=True)[:3]