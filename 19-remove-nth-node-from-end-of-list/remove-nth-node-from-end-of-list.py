class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def size_of(head):
            count = 0
            cur = head
            while cur:
                count += 1
                cur = cur.next
            return count

        length = size_of(head)

        # remove head
        if length == n:
            return head.next

        size = length - n

        cur = head
        prev = None

        while size > 0:
            prev = cur
            cur = cur.next
            size -= 1

        prev.next = cur.next

        return head