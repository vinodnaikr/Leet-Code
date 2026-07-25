class Solution:
    def maxProduct(self, n: int) -> int:
        
        digits = [int(x) for x in str(n)]
        
        digits.sort()
        
        return digits[-1] * digits[-2]