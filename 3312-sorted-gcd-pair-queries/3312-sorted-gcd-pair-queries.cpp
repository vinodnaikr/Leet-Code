#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        
        int max_val = 0;
        for (int num : nums) {
            if (num > max_val) {
                max_val = num;
            }
        }
        
        
        vector<long long> freq(max_val + 1, 0);
        for (int num : nums) {
            freq[num]++;
        }
        
        
        vector<long long> div_count(max_val + 1, 0);
        for (int i = 1; i <= max_val; ++i) {
            for (int j = i; j <= max_val; j += i) {
                div_count[i] += freq[j];
            }
        }
        
       
        vector<long long> exact_gcd(max_val + 1, 0);
        
        for (int i = max_val; i >= 1; --i) {
            long long count = div_count[i];
            
            
            long long pairs = count * (count - 1) / 2;
            
            for (int j = 2 * i; j <= max_val; j += i) {
                pairs -= exact_gcd[j];
            }
            
            exact_gcd[i] = pairs;
        }
        
        
        vector<long long> prefix(max_val + 1, 0);
        for (int i = 1; i <= max_val; ++i) {
            prefix[i] = prefix[i - 1] + exact_gcd[i];
        }
        
        
        vector<int> ans;
        ans.reserve(queries.size()); 
        
        for (long long q : queries) {
            
            auto it = upper_bound(prefix.begin(), prefix.end(), q);
            
            
            ans.push_back(it - prefix.begin());
        }
        
        return ans;
    }
};