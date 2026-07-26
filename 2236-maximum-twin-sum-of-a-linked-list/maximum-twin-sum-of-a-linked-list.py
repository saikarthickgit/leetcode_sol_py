class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        
        # 1. Traversal: Store all values
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        n = len(arr)
        maxi = 0
        
        # 2. Compare twin pairs
        for i in range(n // 2):
            maxi = max(maxi, arr[i] + arr[n - 1 - i])
            
        return maxi