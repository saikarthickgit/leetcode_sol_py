class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        max_char = max(freq, key=freq.get)
        n = len(s)

        if freq[max_char] > (n + 1) // 2:
            return ""

        arr = [""] * n
        i = 0

        # Place the most frequent character at even indices
        while freq[max_char] > 0:
            arr[i] = max_char
            freq[max_char] -= 1
            i += 2

        # Place remaining characters
        for ch in freq:
            while freq[ch] > 0:
                if i >= n:
                    i = 1
                arr[i] = ch
                freq[ch] -= 1
                i += 2

        return "".join(arr)