# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        if len(res) == 1:
            return None
        else:

            res = res[::-1]
            res = res[:n - 1] + res[n:]

            head = None
            for num in res:
                head = ListNode(val=num, next=head)
            return head


l1 = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=4, next=None))))
num = 1
result = Solution().removeNthFromEnd(l1, num)
while result:
    print(result.val, end='')
    result = result.next
