class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
      
        for r in range(rows):
            for c in range(cols):
             
                if matrix[r][c] == 1:
                    heights[c] += 1
                else:
                   
                    heights[c] = 0
            
           
            sorted_heights = sorted(heights, reverse=True)
            
           
            for i in range(cols):
                h = sorted_heights[i]
                w = i + 1
                
                
                if h == 0:
                    break
                    
                current_area = h * w
                max_area = max(max_area, current_area)
                
        return max_area