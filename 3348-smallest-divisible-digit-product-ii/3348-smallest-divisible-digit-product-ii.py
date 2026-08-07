class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def get_factors(n):
            r2 = r3 = r5 = r7 = 0
            while n % 2 == 0: r2 += 1; n //= 2
            while n % 3 == 0: r3 += 1; n //= 3
            while n % 5 == 0: r5 += 1; n //= 5
            while n % 7 == 0: r7 += 1; n //= 7
            if n > 1: return None
            return r2, r3, r5, r7

        factors = get_factors(t)
        if not factors:
            return "-1"
            
        req_2, req_3, req_5, req_7 = factors
        
        fact = [
            (0,0,0,0), (0,0,0,0), (1,0,0,0), (0,1,0,0), (2,0,0,0), 
            (0,0,1,0), (1,1,0,0), (0,0,0,1), (3,0,0,0), (0,2,0,0)
        ]

        dp = [[0] * 45 for _ in range(65)]
        for r2 in range(65):
            for r3 in range(45):
                if r2 == 0 and r3 == 0: continue
                val = float('inf')
                for dr2, dr3 in [(1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2)]:
                    nr2 = r2 - dr2 if r2 > dr2 else 0
                    nr3 = r3 - dr3 if r3 > dr3 else 0
                    # FIX: Prevent DP from referencing its own uninitialized state
                    if nr2 == r2 and nr3 == r3:
                        continue
                    if 1 + dp[nr2][nr3] < val:
                        val = 1 + dp[nr2][nr3]
                dp[r2][r3] = val

        def build_suffix(rem_len, r2, r3, r5, r7):
            res = []
            for pos in range(rem_len):
                if r2 == 0 and r3 == 0 and r5 == 0 and r7 == 0:
                    res.append("1" * (rem_len - pos))
                    break
                    
                for d in range(1, 10):
                    d2, d3, d5, d7 = fact[d]
                    nr2 = r2 - d2 if r2 > d2 else 0
                    nr3 = r3 - d3 if r3 > d3 else 0
                    nr5 = r5 - d5 if r5 > d5 else 0
                    nr7 = r7 - d7 if r7 > d7 else 0
                    
                    spaces_left = rem_len - 1 - pos
                    if nr5 + nr7 + dp[nr2][nr3] <= spaces_left:
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        valid_prefix = [(0, 0, 0, 0)]
        c2 = c3 = c5 = c7 = 0
        for char in num:
            if char == '0':
                break
            d2, d3, d5, d7 = fact[ord(char) - 48]
            c2 += d2; c3 += d3; c5 += d5; c7 += d7
            valid_prefix.append((c2, c3, c5, c7))
            
        N = len(num)
        
        if len(valid_prefix) == N + 1:
            c2, c3, c5, c7 = valid_prefix[-1]
            if c2 >= req_2 and c3 >= req_3 and c5 >= req_5 and c7 >= req_7:
                return num

        for i in range(len(valid_prefix) - 1, -1, -1):
            if i == N: 
                continue
            
            c2, c3, c5, c7 = valid_prefix[i]
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                d2, d3, d5, d7 = fact[d]
                rem_len = N - 1 - i
                
                nr2 = req_2 - c2 - d2 if req_2 > c2 + d2 else 0
                nr3 = req_3 - c3 - d3 if req_3 > c3 + d3 else 0
                nr5 = req_5 - c5 - d5 if req_5 > c5 + d5 else 0
                nr7 = req_7 - c7 - d7 if req_7 > c7 + d7 else 0
                
                if nr5 + nr7 + dp[nr2][nr3] <= rem_len:
                    suffix = build_suffix(rem_len, nr2, nr3, nr5, nr7)
                    return num[:i] + str(d) + suffix

        L = N + 1
        while True:
            if req_5 + req_7 + dp[req_2][req_3] <= L:
                return build_suffix(L, req_2, req_3, req_5, req_7)
            L += 1