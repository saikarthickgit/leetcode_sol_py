class Solution:
    def twoSum(self, num: list[int], target: int) -> list[int]:
        i=0
        j=len(num)-1

        while i<j:
            if num[i]+num[j]==target:
                return [i+1,j+1]
            elif num[i]+num[j]>target:
                j-=1
            else:
                i+=1
        return [i,j]

        