class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = [-1] * len(nums1)

        for i in range(len(nums1)):
            temp = nums1[i]

            # Find temp in nums2
            for j in range(len(nums2)):
                if nums2[j] == temp:

                    # Search to the right
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > temp:
                            result[i] = nums2[k]
                            break
                    break

        return result