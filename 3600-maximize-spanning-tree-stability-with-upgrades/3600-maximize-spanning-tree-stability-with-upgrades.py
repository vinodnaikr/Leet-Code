from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py: return False
                if self.rank[px] < self.rank[py]: px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]: self.rank[px] += 1
                return True
        
        def feasible(mid):
            dsu = DSU(n)
            edges_used = 0
            upgrades_used = 0
            
            # Must-include edges first
            for u, v, s, must in edges:
                if must == 1:
                    if s < mid:
                        return False  # too weak, can't upgrade
                    if not dsu.union(u, v):
                        return False  # cycle among must-edges
                    edges_used += 1
            
            # Free optional edges (no upgrade needed)
            for u, v, s, must in edges:
                if must == 0 and s >= mid:
                    if dsu.union(u, v):
                        edges_used += 1
            
            # Costly optional edges (need 1 upgrade each)
            for u, v, s, must in edges:
                if must == 0 and s * 2 >= mid and s < mid:
                    if upgrades_used < k and dsu.union(u, v):
                        edges_used += 1
                        upgrades_used += 1
            
            return edges_used == n - 1
        
        # Check if any spanning tree exists at all (mid=0)
        if not feasible(0):
            return -1
        
        # Collect all possible strength values (original + doubled)
        candidates = set()
        for u, v, s, must in edges:
            candidates.add(s)
            if must == 0:
                candidates.add(s * 2)
        candidates.add(0)
        candidates = sorted(candidates)
        
        # Binary search over candidate values
        lo, hi = 0, len(candidates) - 1
        ans = 0
        while lo <= hi:
            m = (lo + hi) // 2
            if feasible(candidates[m]):
                ans = candidates[m]
                lo = m + 1
            else:
                hi = m - 1
        
        return ans