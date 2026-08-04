class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_value = max(nums)
        missing = []
        num_set = set(nums)

        for num in range(min_val,max_value+1):
            if num not in num_set:
                missing.append(num)

        
        return missing