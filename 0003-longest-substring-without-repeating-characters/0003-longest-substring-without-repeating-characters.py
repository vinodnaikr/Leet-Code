class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest=[]
        left=0
        max_length=0
        for i in range(len(s)):
            while s[i] in longest:
                longest.remove(s[left])
                left=left+1
            longest.append(s[i])
            max_length=max(max_length,i-left+1)
        return max_length