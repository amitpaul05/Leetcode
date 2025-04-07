class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        currCount, ans = 0, 0

        for i in range(len(s)):
            if i >= k and s[i - k] in vowels :
                currCount -= 1
            currCount += s[i] in vowels
            ans = max(currCount, ans)

        return ans