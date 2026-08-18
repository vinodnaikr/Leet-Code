class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();  
        if (n == 1) return 0;
        
        vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                int total = prefix[j + 1] - prefix[i];
                
                int maxScore = 0;
                int leftSum = 0;
                
                for (int k = i; k < j; k++) {
                    leftSum += stoneValue[k];
                    int rightSum = total - leftSum;
                    
                    int score;
                    if (leftSum < rightSum) {
                        score = leftSum + dp[i][k];
                    } else if (leftSum > rightSum) {
                        score = rightSum + dp[k + 1][j];
                    } else {
                        score = leftSum + max(dp[i][k], dp[k + 1][j]);
                    }
                    
                    maxScore = max(maxScore, score);
                }
                
                dp[i][j] = maxScore;
            }
        }
        
        return dp[0][n - 1];
    }
};