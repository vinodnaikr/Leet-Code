class Solution(object):
    def minOperations(self, s):
        count=0
        n=len(s)

        for i in range(n):
            if i%2==0:
                if s[i]!='0':
                    count+=1
            else:
                if s[i]!='1':
                    count+=1
        
        return min(count,n-count)