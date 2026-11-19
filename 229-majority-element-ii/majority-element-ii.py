class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums) 
        cnt_1=0
        cnt_2=0
        num2=None
        num1=None
    

        for num in nums:
            if num==num1:
                cnt_1+=1
            elif num==num2:
                cnt_2+=1
            elif cnt_1==0:
                num1=num
                cnt_1=1
            elif cnt_2==0:
                cnt_2=1
                num2=num
            else:
                cnt_1-=1
                cnt_2-=1
        
        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res
            
