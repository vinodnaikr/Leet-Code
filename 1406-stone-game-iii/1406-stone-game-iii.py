class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*4

        for i in range(n-1,-1,-1):
            current_sum = 0
            dp[i%4] = float('-inf')

            for k in range(1,4):
                if i+k <= n:
                    current_sum+=stoneValue[i+k-1]
                    dp[i%4] = max(dp[i%4],current_sum-dp[(i+k)%4])
        
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        else:
            return "Tie"
        