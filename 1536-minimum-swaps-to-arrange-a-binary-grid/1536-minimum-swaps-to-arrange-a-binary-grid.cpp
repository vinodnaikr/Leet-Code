class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> trailing_zeros;

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) {
                    count++;
                } else {
                    break;
                }
            }
            trailing_zeros.push_back(count);
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            int target = n - i - 1;
            int found = -1;

            for (int j = i; j < n; j++) {
                if (trailing_zeros[j] >= target) {
                    found = j;
                    break;
                }
            }

            if (found == -1) return -1;

            for (int j = found; j > i; j--) {
                swap(trailing_zeros[j], trailing_zeros[j - 1]);
                swaps++;
            }
        }

        return swaps;
    }
};