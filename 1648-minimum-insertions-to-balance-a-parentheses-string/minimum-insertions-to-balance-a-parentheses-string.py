class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == "(":
                stack.append("(")
            else: # s[i] == ")"
                # Check if we have a double '))'
                if i + 1 < n and s[i+1] == ")":
                    i += 1 # We have '))', skip the next index
                else:
                    count += 1 # We only had one ')', we need to insert another ')'
                    
                # Now try to match this '))' with a '(' from the stack
                if stack:
                    stack.pop() # Match found
                else:
                    count += 1 # No '(' in stack, we must insert one
            i += 1
            
        # For any '(' left in the stack, we need to insert two ')'
        return count + (len(stack) * 2)