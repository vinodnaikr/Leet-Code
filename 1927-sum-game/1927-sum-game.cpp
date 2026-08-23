class Solution {
public:
    bool sumGame(string num) {
        int n = num.length();
        int mid = n / 2;
        
        int sumL = 0, sumR = 0;
        int qL = 0, qR = 0;
        
        for (int i = 0; i < mid; i++) {
            if (num[i] == '?') qL++;
            else sumL += num[i] - '0';
        }
        
        for (int i = mid; i < n; i++) {
            if (num[i] == '?') qR++;
            else sumR += num[i] - '0';
        }
        
        int diff = sumL - sumR;
        
        
        return 2 * diff != 9 * (qR - qL);
    }
};