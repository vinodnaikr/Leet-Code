import bisect
from collections import deque

class Solution:
    def minOperations(self, s, k):
        n = len(s)
        cnt0 = s.count('0')
        if cnt0 == 0:
            return 0
        
        # Parity lists: store all possible counts of zeros [0...n]
        # split by even and odd to satisfy the parity constraint.
        available = [[], []]
        for i in range(n + 1):
            available[i % 2].append(i)
        
        # Remove the starting count from available
        idx = bisect.bisect_left(available[cnt0 % 2], cnt0)
        available[cnt0 % 2].pop(idx)
        
        queue = deque([cnt0])
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                # Minimum zeros: flip as many 0s as possible, min(cur, k)
                # Maximum zeros: flip as many 1s as possible, min(n - cur, k)
                # Range of x (zeros flipped): [max(0, k - (n - cur)), min(cur, k)]
                # Range of new_z: [cur + k - 2*min(cur, k), cur + k - 2*max(0, k-n+cur)]
                
                L = cur + k - 2 * min(cur, k)
                R = cur + k - 2 * max(0, k - n + cur)
                
                if L == 0:
                    return steps
                
                
                target_list = available[L % 2]
                left_idx = bisect.bisect_left(target_list, L)
                right_idx = bisect.bisect_right(target_list, R)
                
                
                for i in range(left_idx, right_idx):
                    val = target_list[i]
                    if val == 0:
                        return steps
                    queue.append(val)
                
               
                del target_list[left_idx:right_idx]
                    
        return -1