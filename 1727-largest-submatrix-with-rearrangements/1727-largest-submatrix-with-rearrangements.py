class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # This list tracks the 'tower height' for each column
        heights = [0] * cols
        max_area = 0
        
        # We start from Row 0 and process every row
        for r in range(rows):
            for c in range(cols):
                # If current cell is 1, the tower grows
                if matrix[r][c] == 1:
                    heights[c] += 1
                else:
                    # If current cell is 0, the tower breaks
                    heights[c] = 0
            
            # Now we have a list of heights for the current row.
            # Sort them in descending order to group the tallest ones together.
            sorted_heights = sorted(heights, reverse=True)
            
            # Calculate the area for every possible width at this row
            for i in range(cols):
                h = sorted_heights[i]
                w = i + 1
                
                # If we hit a height of 0, no more rectangles can be formed here
                if h == 0:
                    break
                    
                current_area = h * w
                max_area = max(max_area, current_area)
                
        return max_area