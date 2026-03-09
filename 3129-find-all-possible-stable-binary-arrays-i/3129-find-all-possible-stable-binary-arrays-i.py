class Solution:
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        # dp[i][j][0] means i zeros, j ones, ending in 0
        # dp[i][j][1] means i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        # Base cases: single sequences within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Ending in 0:
                # We can append 0 to any valid array ending in 0 or 1
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # Subtract arrays that already had 'limit' zeros consecutively
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD

                # Ending in 1:
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # Subtract arrays that already had 'limit' ones consecutively
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD