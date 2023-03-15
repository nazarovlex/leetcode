# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
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
            c[-2] %= 10
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


# list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9, next=None)))
# list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=ListNode(val=9, next=None))))
# list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
# list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
list1 = ListNode(val=5, next=None)
list2 = ListNode(val=5, next=None)

s = Solution()
result = s.addTwoNumbers(list1, list2)

while result:
    print(result.val)
    result = result.next
