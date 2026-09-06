class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Minimum total cost to be ready to leave step 0 and step 1
        prev2 = cost[0]
        prev1 = cost[1]

        # Calculate best cost for all subsequent steps
        for i in range(2, len(cost)):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current

        # You can reach the top from either the last step or the second-to-last step
        return min(prev1, prev2)