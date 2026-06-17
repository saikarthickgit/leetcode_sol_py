class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        left = 0
        maxi = 0

        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1

            while a[s[i]] > 1:
                a[s[left]] -= 1
                left += 1

            maxi = max(maxi, i - left + 1)

        return maxi