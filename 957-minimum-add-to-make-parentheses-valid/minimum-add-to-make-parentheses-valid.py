class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0   
        count1 = 0  
        
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                if count > 0:
                   
                    count -= 1
                else:
                  
                    count1 += 1
                    
      
        return count + count1