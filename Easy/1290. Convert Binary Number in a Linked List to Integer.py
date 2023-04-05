class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ""
        while head:
            num = num + str(head.val)
            head = head.next
        return int(num, 2)


head = ListNode(val=1, next=ListNode(val=0, next=ListNode(val=1)))
result = Solution().getDecimalValue(head)
print(result)
