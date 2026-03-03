class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        for(int val: nums){
            int freq=0;
            for(int ele: nums){
                if(val==ele){
                    freq++;
                }
            }
            if(freq>n/2){
                return val;
            }
        }
        return -1;

    }
};