class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        
        reachable_1 = set(nums)
        
        reachable_2 = set()
        for x in reachable_1:
            for y in nums:
                reachable_2.add(x ^ y)
                
        reachable_3 = set()
        for xy in reachable_2:
            for z in nums:
                reachable_3.add(xy ^ z)
                
        
        return len(reachable_3)
