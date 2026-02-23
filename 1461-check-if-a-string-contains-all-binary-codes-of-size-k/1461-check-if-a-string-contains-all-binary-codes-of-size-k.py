class Solution(object):
    def hasAllCodes(self, s, k):

        sub_strings=set()

        for i in range(len(s)-k+1):
            current_string=s[i:i+k]
            sub_strings.add(current_string)

        total=2**k

        if len(sub_strings)==total:
            return True
        else:
            return False

         