class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                m = nums[i] % n
                if i + m < n:
                    result.append(nums[i + m])
                else:
                    result.append(nums[(i + m) % n])
            else:
                m = (-nums[i]) % n
                if i - m >= 0:
                    result.append(nums[i - m])
                else:
                    result.append(nums[(i - m) % n])

        return result