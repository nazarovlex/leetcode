# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        head2 = head
        while head.next and head.next.next:
            if head2 == head.next or head2 == head.next.next:
                return True
            head2 = head2.next
            head = head.next.next
        return False


list_ar = [5, 7, 5]
h = ListNode(val=1)
cnt = 0
while cnt < 5:
    h = ListNode(val=list_ar[cnt % 2], next=h)
    cnt += 1

h = ListNode(val=1, next=h)

result = Solution().hasCycle(h)
print(result)
