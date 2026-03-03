class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr_sum=0;
        int max_sum=INT_MIN;
        for(int val:nums){
            curr_sum+=val;
            max_sum=max(curr_sum,max_sum);
            if(curr_sum<0){
                curr_sum=0;
            }
        }
        return max_sum;
        
    }
};