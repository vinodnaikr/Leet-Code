class Solution(object):
    def minFlips(self, s):
        n=len(s)
        ans=n
        double_s=s+s
        diff=0
        for i in range(2*n):
            if i%2==0:
                expected='0'
            else:
                expected='1'
            
            if double_s[i]!=expected:
                diff+=1

            if i>=n:
                if (i-n)%2==0:
                    left_expected='0'
                else:
                    left_expected='1'

                if double_s[i-n]!=left_expected:
                    diff-=1
            
            if i>=n-1:
                ans=min(ans,diff,n-diff)
        return ans