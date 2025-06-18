class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        for i in reversed(s.split()):
            res = res + i + ' '
        res = res[:-1]
        return res 