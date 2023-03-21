from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # solution with extra memory
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        mas = []
        while head:
            mas.append(head.val)
            head = head.next

        while True:
            if mas.count(value)>0:
                mas.remove(value)
            else:
                break
        mas = mas[::-1]
        head = None
        i = 0
        while i<len(mas):
            head = ListNode(val=mas[i], next=head)
            i += 1
        return head


class Solution2: # recursion solution
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.val == val:
            head = head.next
            head = self.removeElements(head, val)
        elif head.val != val:
            head.next = self.removeElements(head.next, val)
        return head


l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=6, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6, next=None)))))))
value = 6
result = Solution().removeElements(l1, value)
while result:
    print(result.val,end='')
    result = result.next
print()
result = Solution2().removeElements(l1, value)
while result:
    print(result.val,end='')
    result = result.next
