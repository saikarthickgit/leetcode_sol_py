class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if m<n:
            return False
        target = Counter(s1)
        window = Counter(s2[:n])

        if window == target:
            return True

        for i in range(n, m):
           
            window[s2[i]] += 1 # Add new character

           
            left = s2[i - n] # Remove leftmost character
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if window == target:
                return True

        return False