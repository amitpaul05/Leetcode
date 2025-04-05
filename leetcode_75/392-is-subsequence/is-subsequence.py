class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        s_len = 0 # number of matched char
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                s_len += 1
                j += 1
        
        return s_len == len(s)