class Solution(object):
    def makeLargestSpecial(self, s):
        def make_largest(s):
            if not s:
                return ""
            count = 0
            start = 0
            substrings = []
            for i, ch in enumerate(s):
                count += 1 if ch == '1' else -1
                if count == 0:
                    
                    inner = make_largest(s[start+1:i])
                    substrings.append("1" + inner + "0")
                    start = i + 1
           
            substrings.sort(reverse=True)
            return "".join(substrings)

        return make_largest(s)