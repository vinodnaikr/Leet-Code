
class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        long long low = 1;
        long long min_wt = *min_element(workerTimes.begin(), workerTimes.end());
        long long high = min_wt * (long long)mountainHeight * (mountainHeight + 1) / 2;
        
        long long ans = high;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (canReduce(mid, mountainHeight, workerTimes)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }


    bool canReduce(long long t, int targetHeight, const vector<int>& workerTimes) {
        long long totalReduction = 0;
        for (int wt : workerTimes) {
            long long x = (-1 + sqrt(1 + (8.0 * t) / wt)) / 2;
            totalReduction += x;
            
            if (totalReduction >= targetHeight) return true;
        }
        return totalReduction >= targetHeight;
    }
};