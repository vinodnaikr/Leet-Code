class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();
        
        // Precompute all subset LCMs
        vector<pair<long long, int>> subsets;
        for (int mask = 1; mask < (1 << n); mask++) {
            long long lcm = 1;
            int size = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    size++;
                    lcm = lcm * coins[i] / std::gcd(lcm, (long long)coins[i]);
                    if (lcm > 1e15) {
                        lcm = 1e15 + 1;
                        break;
                    }
                }
            }
            subsets.push_back({lcm, size});
        }
        
        auto count = [&](long long x) -> long long {
            long long total = 0;
            for (auto& [lcm, size] : subsets) {
                if (lcm <= x) {
                    if (size % 2 == 1) {
                        total += x / lcm;
                    } else {
                        total -= x / lcm;
                    }
                }
            }
            return total;
        };
        
        // Binary search
        long long left = 1;
        long long right = 1LL * *min_element(coins.begin(), coins.end()) * k;
        
        while (left < right) {
            long long mid = left + (right - left) / 2;
            if (count(mid) >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
};