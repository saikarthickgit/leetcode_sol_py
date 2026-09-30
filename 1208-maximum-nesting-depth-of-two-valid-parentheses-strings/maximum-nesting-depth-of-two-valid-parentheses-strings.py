class Solution:
    def maxDepthAfterSplit(self, seq):
        n = len(seq)
        r = [0] * n
        depth = 0
        for i in range(n):
            if seq[i] == '(':
              
                depth += 1
                r[i] = depth & 1
                continue
            
            r[i] = depth & 1
            depth -= 1
        return r