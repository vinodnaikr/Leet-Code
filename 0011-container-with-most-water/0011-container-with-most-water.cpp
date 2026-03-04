class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxWater=0;
        int i=0;
        int n=height.size();
        int j=n-1;
        while(i<j){
            int w=j-i;
            int ht=min(height[i],height[j]);
            int currWater=w*ht;
            maxWater=max(maxWater,currWater);

            height[i]<height[j] ? i++:j--;
        }
        return maxWater;
        
    }
};