class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

     
        threshold = len(nums) // 3

        if cand1 is not None and nums.count(cand1) > threshold:
            ans.append(cand1)

        if cand2 is not None and nums.count(cand2) > threshold:
            ans.append(cand2)

        return ans
        