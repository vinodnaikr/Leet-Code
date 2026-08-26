class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.length();
        string ans = "";
        
        for (int i = 0; i < n; i++) {
            int ones = 0;
            
            
            for (int j = i; j < n; j++) {
                if (s[j] == '1') {
                    ones++;
                }
                
                if (ones == k) {
                    
                    string candidate = s.substr(i, j - i + 1);
                    
                    
                    if (ans.empty() || 
                        candidate.length() < ans.length() || 
                        (candidate.length() == ans.length() && candidate < ans)) {
                        ans = candidate;
                    }
                    
                    
                    break;
                }
            }
        }
        
        return ans;
    }
};