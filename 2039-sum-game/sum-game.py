class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        left = num[:n // 2]
        right = num[n // 2:]
        
        l_sum = 0
        r_sum = 0
        count_l = 0
        count_r = 0
        
        for i in left:
            if i == "?":
                count_l += 1
            else:
                l_sum += int(i)
                
        for i in right:
            if i == "?":
                count_r += 1
            else:
                r_sum += int(i)
                
        return 2 * (l_sum - r_sum) != 9 * (count_r - count_l)