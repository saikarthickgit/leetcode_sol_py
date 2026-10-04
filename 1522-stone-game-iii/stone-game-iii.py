class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
       
        memo = [None] * n 
        
        def play(i):
            
            if i >= n:
                return (0, 0)
            
            
            if memo[i] is not None:
                return memo[i]
            
            best_my_score = float('-inf')
            best_opp_score = 0
            current_take_sum = 0
         
            for k in range(1, min(4, n - i + 1)):
                current_take_sum += stoneValue[i + k - 1]
                
               
                opp_future_score, my_future_score = play(i + k)
                
               
                my_total_score = current_take_sum + my_future_score
                
               
                if my_total_score > best_my_score:
                    best_my_score = my_total_score
                    best_opp_score = opp_future_score
                    
            
            memo[i] = (best_my_score, best_opp_score)
            return memo[i]

        
        alice_score, bob_score = play(0)
        
       
        if alice_score > bob_score:
            return "Alice"
        elif bob_score > alice_score:
            return "Bob"
        else:
            return "Tie"