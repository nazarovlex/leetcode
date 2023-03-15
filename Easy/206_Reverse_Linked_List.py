# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        nl = None
        while head:
            print(head.val)
            nl = ListNode(val=head.val, next=nl)
            head = head.next

        return nl


l1 = ListNode(val=1, next=ListNode(val=5, next=ListNode(val=6, next=None)))
result = Solution().reverseList(l1)
while result:
    print(result.val)
    result = result.next
print(result)
