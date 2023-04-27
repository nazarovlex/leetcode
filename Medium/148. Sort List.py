from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        list.sort()
        head = None
        for num in list[::-1]:
            head = ListNode(val=num, next=head)
        return head


ln = ListNode(val=5, next=ListNode(val=4, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=1, next=ListNode(val=6))))))
result = Solution().sortList(ln)
while result:
    print(result.val)
    result = result.next
