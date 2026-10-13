class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {

        int n = nums.size();

        vector<long long> squares(n);

        for(int i = 0; i < n; ++i){
            squares[i] = 1LL*nums[i]*nums[i];
        }

        sort(squares.begin(),squares.end());

        int k = n/2;

        long long negSum = 0;
        long long posSum = 0;

        for(int i = 0; i < k; ++i){
            negSum += squares[i];
        }

        for(int i = k ; i < n; ++i){
            posSum += squares[i];
        }

        return posSum-negSum;
        
    }
};