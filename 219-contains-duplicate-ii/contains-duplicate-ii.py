class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        res = {}

        for i, n in enumerate(nums):
            temp = i

            if n in res:
                temp2 = res.get(n)
                temp3 = temp - temp2

                if temp3 <= k:
                    return True

            res[n] = i

        return False