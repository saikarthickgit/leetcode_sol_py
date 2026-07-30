class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        dummy=head
        slow=dummy
        fast=dummy
        prev,temp=None,None

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
    
        prev.next=slow.next
        return dummy




       