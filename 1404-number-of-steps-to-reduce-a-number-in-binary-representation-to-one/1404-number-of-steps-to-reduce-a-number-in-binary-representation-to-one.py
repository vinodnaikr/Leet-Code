class Solution(object):
    def numSteps(self, s):
        n=int(s,2)
        steps=0
        
        while n!=1:
            if n%2==0:
                n=n/2
                steps=steps+1
            elif n%2!=0:
                n=n+1
                steps=steps+1
        return steps