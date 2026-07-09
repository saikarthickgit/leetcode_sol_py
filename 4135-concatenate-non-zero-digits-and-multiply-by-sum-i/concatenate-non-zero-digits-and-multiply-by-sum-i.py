class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum = 0
        temp = ""
        s = str(n)

        for i in range(len(s)):
            if int(s[i]) > 0:
                digit_sum += int(s[i])
                temp += s[i]

        if temp == "":
            return 0

        return int(temp) * digit_sum