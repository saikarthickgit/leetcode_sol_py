class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp=[]
        n=len(nums)
        t=n//3
        c=Counter(nums)
        for i, j in c.items():
            if j >t:
                temp.append(i)
        return temp


        
        

        