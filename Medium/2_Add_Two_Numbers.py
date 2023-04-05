# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object): # Brutal solution with array
    def addTwoNumbers(self, l1, l2):
        ln = None
        c = []

        while l1 or l2:
            if l1 is not None and l2 is not None:
                c.append(l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1 is None:
                c.append(l2.val)
                l2 = l2.next
            elif l2 is None:
                c.append(l1.val)
                l1 = l1.next

        if len(c) == 1 and c[0] < 10:
            return ListNode(val=c[0])
        elif len(c) == 1 and c[0] >= 10:
            c.append(c[-1] // 10)
            c[0] %= 10
            return ListNode(val=c[0], next=ListNode(val=c[1], next=None))
        for i in range(1, len(c)):
            if c[i - 1] >= 10:
                c[i] += c[i - 1] // 10
                c[i - 1] %= 10
        if c[-1] >= 10:
            c.append(c[-1] // 10)
            c[-2] %= 10

        for i in range(len(c) - 1, -1, -1):
            ln = ListNode(val=c[i], next=ln)

        return ln

class Solution2: # Solution with cursor
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next



list1 = ListNode(val=5, next=None)
list2 = ListNode(val=5, next=None)

s = Solution()
result = s.addTwoNumbers(list1, list2)

while result:
    print(result.val)
    result = result.next
