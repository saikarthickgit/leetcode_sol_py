class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == "(":
                stack.append("(")
            else: 
                if i + 1 < n and s[i+1] == ")":
                    i += 1 
                else:
                    count += 1
                    
               
                if stack:
                    stack.pop() 
                else:
                    count += 1 
            i += 1
            
   
        return count + (len(stack) * 2)