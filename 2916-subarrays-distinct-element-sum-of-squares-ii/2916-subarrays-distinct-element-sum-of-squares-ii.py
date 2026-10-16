class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        
        sum1 = [0] * (4 * n)  
        sum2 = [0] * (4 * n)  
        lazy = [0] * (4 * n)  
        
        
        def apply(node: int, l: int, r: int, v: int):
            length = r - l + 1
            
            sum2[node] = (sum2[node] + 2 * v * sum1[node] + length * v * v) % MOD
            
            sum1[node] = (sum1[node] + length * v) % MOD
            
            lazy[node] = (lazy[node] + v) % MOD

        
        def push(node: int, l: int, r: int):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(node * 2, l, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, r, lazy[node])
                lazy[node] = 0  

        
        def update(node: int, l: int, r: int, ql: int, qr: int, v: int):
            
            if ql <= l and r <= qr:
                apply(node, l, r, v)
                return
            
            
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, v)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, v)
            
            
            sum1[node] = (sum1[node * 2] + sum1[node * 2 + 1]) % MOD
            sum2[node] = (sum2[node * 2] + sum2[node * 2 + 1]) % MOD

        
        last_seen = {}
        total_ans = 0
        
        for r, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            
            
            update(1, 0, n - 1, prev + 1, r, 1)
            
            
            total_ans = (total_ans + sum2[1]) % MOD
            
            last_seen[x] = r
            
        return total_ans