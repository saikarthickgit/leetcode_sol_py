
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        arr[a - 1].next = list2

        cur = list2
        while cur.next:
            cur = cur.next

        cur.next = arr[b + 1]
        return list1