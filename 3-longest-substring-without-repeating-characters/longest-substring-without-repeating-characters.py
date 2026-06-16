class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = ""
        maxi = 0

        for i in range(len(s)):
            while s[i] in t:
                t = t[1:]

            t += s[i]
            maxi = max(maxi, len(t))

        return maxi