# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        return num == num[::-1]


list1 = ListNode(val=1, next=ListNode(val=5, next=ListNode(val=1, next=None)))
result = Solution().isPalindrome(list1)
print(result)
