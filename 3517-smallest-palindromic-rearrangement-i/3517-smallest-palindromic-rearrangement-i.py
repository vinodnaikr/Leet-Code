from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        freq = Counter(s)
        
        left_half = []
        middle = ""
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq[char] > 0:
                
                if freq[char] % 2 != 0:
                    middle = char
                
               
                left_half.append(char * (freq[char] // 2))
                
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]