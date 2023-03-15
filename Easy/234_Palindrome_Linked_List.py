# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        head_array = []
        while head:
            head_array.append(head.val)
            head = head.next
        if head_array == head_array[::-1]:
            return True
        else:
            return False


list1 = ListNode(val=1, next=ListNode(val=5, next=ListNode(val=1, next=None)))
result = Solution().isPalindrome(list1)
print(result)
