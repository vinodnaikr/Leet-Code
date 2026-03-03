class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // sort
        sort(nums.begin(),nums.end());

        //freq count
        int freq=1,ans=nums[0];
        int n=nums.size();

        for(int i=1;i<n;i++){
            if(nums[i]==nums[i-1]){
                freq++;
            }
            else{
                freq=1;
                ans=nums[i];
            }
            if(freq>n/2){
                return ans;
            }

        }
        return ans;
    }
};