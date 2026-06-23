class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_idx = height.index(max(height))
        water = 0

        left_max = height[0]
        for i in range(1, max_idx):
            left_max = max(left_max, height[i])
            water += left_max - height[i]

        right_max = height[-1]
        for i in range(len(height)-2, max_idx, -1):
            right_max = max(right_max, height[i])
            water += right_max - height[i]

        return water