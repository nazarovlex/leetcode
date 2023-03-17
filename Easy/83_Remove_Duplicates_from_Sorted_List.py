from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        box = []
        while head:
            if head.val not in box:
                box.append(head.val)
                head = head.next
            else:
                head = head.next

        while len(box) > 0:
            head = ListNode(val=box[-1], next=head)
            box.pop(-1)
        return head


l1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=None)))
result = Solution().deleteDuplicates(l1)
while result:
    print(result.val)
    result = result.next
