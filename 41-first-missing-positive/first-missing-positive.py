class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        expected = 1

        for i in nums:
            if i > 0 and i == expected:
                expected += 1

        return expected