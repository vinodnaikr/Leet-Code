class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if(sum>9LL*num){
            return "";
        }

        int nines = sum/9;
        int rem = sum%9;

        string ans = "";

        for(int i=0;i<nines;++i){
            ans.push_back('9');


        }
        if(rem>0){
            ans.push_back('0'+rem);
        }

        while(ans.length()<num){
            ans.push_back('0');
        }

        return ans;
    }
};