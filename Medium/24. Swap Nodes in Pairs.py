# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        for i in range(0, len(res) - 1, 2):
            res[i], res[i + 1] = res[i + 1], res[i]

        head = None
        for num in res[::-1]:
            head = ListNode(val=num, next=head)
        return head


l1 = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=4, next=ListNode(val=5,
                                                                                                  next=ListNode(val=6,
                                                                                                                next=None))))))
result = Solution().swapPairs(l1)
while result:
    print(result.val, end='')
    result = result.next
