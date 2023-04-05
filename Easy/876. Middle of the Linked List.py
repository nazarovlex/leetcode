from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # Solution with cursor
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        nh = head
        while nh:
            length += 1
            nh = nh.next
        for _ in range(length // 2):
            head = head.next
        return head


class Solution2:  # Solution with array
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mas = []
        while head:
            mas.append(head.val)
            head = head.next
        head = None
        for num in mas[len(mas) // 2:][::-1]:
            head = ListNode(val=num, next=head)
        return head


head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
result = Solution().middleNode(head)
while result:
    print(result.val)
    result = result.next
