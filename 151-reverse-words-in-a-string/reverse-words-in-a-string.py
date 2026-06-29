class Solution:
    def reverseWords(self, s: str) -> str:

        stack = []
        temp = ""
        result = ""

        for ch in s:
            if ch == " ":
                if temp:          # Only push non-empty words
                    stack.append(temp)
                    temp = ""
            else:
                temp += ch

        if temp:
            stack.append(temp)

        while stack:
            result += stack.pop()
            if stack:
                result += " "

        return result