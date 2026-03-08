class Solution(object):
    def findDifferentBinaryString(self,nums):
     n = len(nums)
     result = []
    
     for i in range(n):
        
         current_char = nums[i][i]
         result.append('1' if current_char == '0' else '0')
    
     return ''.join(result)