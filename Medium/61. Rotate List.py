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


class Solution2:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        pntr = head
        length = 1
        while pntr.next:
            length += 1
            pntr = pntr.next
        k = k % length
        pntr.next = head
        tempNode = head

        for _ in range(length - k - 1):
            tempNode = tempNode.next

        head = tempNode.next

        tempNode.next = None

        return head


l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
k = 4
result1 = Solution().rotateRight(l1, k)
result2 = Solution2().rotateRight(l1, k)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
