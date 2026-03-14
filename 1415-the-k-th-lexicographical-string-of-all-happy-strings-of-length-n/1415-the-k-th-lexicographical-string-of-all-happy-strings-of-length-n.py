class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_per_start = 1<<(n-1)

        if k>3*total_per_start:
            return ""
        
        res = []
        choices = ['a','b','c']
        index = (k-1)//total_per_start
        res.append(choices[index])
        k = (k-1)%total_per_start+1

        for i in range(1,n):
            total_per_start//=2
            current_choices = [c for c in choices if c != res[-1]]
            index = (k-1)//total_per_start
            res.append(current_choices[index])
            k = (k-1)%total_per_start + 1
            
        return "".join(res)