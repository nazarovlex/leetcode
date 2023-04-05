# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


l1 = ListNode(val=1, next=ListNode(val=5, next=ListNode(val=6, next=None)))
result = Solution().reverseList(l1)
while result:
    print(result.val)
    result = result.next
