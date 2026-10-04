class Solution:
    def checkValidString(self, s: str) -> bool:
        sumi = 0
        count = 0 # Initialize count

        # 1. Your left-to-right pass (checks for too many ')')
        for i in s: # Iterate over the string, not the length
            if i == "(":
                sumi += 1
            elif i == ")":
                sumi -= 1
            else:
                count += 1
            
            # If closing brackets exceed open brackets + stars, it's invalid
            if sumi + count < 0:
                return False

        sumi = 0
        count = 0
        
        # 2. Right-to-left pass (checks for too many '(')
        for i in reversed(s):
            if i == ")":
                sumi += 1
            elif i == "(":
                sumi -= 1
            else:
                count += 1
            
            # If opening brackets exceed closing brackets + stars, it's invalid
            if sumi + count < 0:
                return False
                
        return True