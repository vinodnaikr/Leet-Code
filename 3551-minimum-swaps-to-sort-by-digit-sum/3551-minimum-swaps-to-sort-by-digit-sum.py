class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def get_digit_sum(num: int) -> int:
            total = 0
            while num>0:
                total += num%10
                num //= 10
            
            return total

        n = len(nums)
        sorted_nums = sorted(nums,key=lambda x: (get_digit_sum(x),x))

        num_to_index = {val: i for i,val in enumerate(sorted_nums)}

        visited = [False]*n
        min_swaps = 0

        for i in range(n):
            if visited[i] or num_to_index[nums[i]] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = num_to_index[nums[j]]
                cycle_size += 1

            min_swaps += (cycle_size-1)
        
        return min_swaps

        