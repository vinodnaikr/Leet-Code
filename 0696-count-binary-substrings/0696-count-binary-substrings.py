class Solution(object):
    def countBinarySubstrings(self,s):
     ans = 0
     prev = 0
     cur = 1
     for i in range(1, len(s)):
        if s[i-1] != s[i]:
            
            ans += min(prev, cur) 
    
            prev, cur = cur, 1    
        else:
        
            cur += 1
     return ans + min(prev, cur)