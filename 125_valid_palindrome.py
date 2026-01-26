class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()

        reverse_s = new_s[::-1]
        return new_s == reverse_s