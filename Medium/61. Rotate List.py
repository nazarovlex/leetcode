from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next

        if k > len(res):
            k = k % len(res)

        while k:
            res.insert(0, res[-1])
            res.pop()
            k -= 1
        head = None
        for num in res[::-1]:
            head = ListNode(val=num, next=head)

        return head


l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
k = 2000000000
result = Solution().rotateRight(l1, k)
while result:
    print(result.val, end=" ")
    result = result.next
