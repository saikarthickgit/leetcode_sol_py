class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        ans = 0
        st = []

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                idx = st.pop()

                left = st[-1] if st else -1
                width = i - left - 1

                ans = max(ans, heights[idx] * width)

            st.append(i)

        while st:
            idx = st.pop()

            left = st[-1] if st else -1
            width = n - left - 1

            ans = max(ans, heights[idx] * width)

        return ans