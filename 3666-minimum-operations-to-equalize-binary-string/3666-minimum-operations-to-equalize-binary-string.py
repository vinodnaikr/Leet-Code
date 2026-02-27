
class Solution:
    def minOperations(self, s, k):
        n = len(s)
        cnt0 = s.count('0')
        if cnt0 == 0:
            return 0
        
        available = [[], []]
        for i in range(n + 1):
            available[i % 2].append(i)
        
        target_list = available[cnt0 % 2]
        idx = bisect.bisect_left(target_list, cnt0)
        if idx < len(target_list) and target_list[idx] == cnt0:
            target_list.pop(idx)
        
        queue = deque([cnt0])
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                L = abs(cur - k)
                R = n - abs(n - (cur + k))
                
                if L == 0:
                    return steps
                
                target_parity = available[L % 2]
                left_idx = bisect.bisect_left(target_parity, L)
                right_idx = bisect.bisect_right(target_parity, R)
                
                if left_idx < right_idx:
                    for i in range(left_idx, right_idx):
                        val = target_parity[i]
                        if val == 0:
                            return steps
                        queue.append(val)
                    del target_parity[left_idx:right_idx]
                    
        return -1