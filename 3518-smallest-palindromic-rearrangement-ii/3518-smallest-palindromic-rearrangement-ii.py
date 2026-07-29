class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        
        freq = Counter(s)
        
        odd_chars = [char for char, count in freq.items() if count % 2 != 0]
        mid_char = odd_chars[0] if odd_chars else ""
        
        half_counts = [0] * 26
        for char, count in freq.items():
            half_counts[ord(char) - ord('a')] = count // 2
            
        def count_arrangements(counts, limit=10**6 + 1):
            
            valid_counts = [c for c in counts if c > 0]
            if not valid_counts:
                return 1
            
            valid_counts.sort(reverse=True)
            
            res = 1
            total_remaining = sum(valid_counts)
            
            for c in valid_counts[1:]:
                for i in range(1, c + 1):
                    res = res * total_remaining // i
                    total_remaining -= 1
                    
                    if res >= limit:
                        return limit
            return res
        
        total_perms = count_arrangements(half_counts)
        if total_perms < k:
            return ""
            
        left_half = []
        half_len = sum(half_counts)
        
        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] > 0:
                    half_counts[i] -= 1
                    perms = count_arrangements(half_counts)
                    
                    if perms >= k:
                        
                        left_half.append(chr(i + ord('a')))
                        break
                    else:
                        
                        k -= perms
                        half_counts[i] += 1
                        
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]