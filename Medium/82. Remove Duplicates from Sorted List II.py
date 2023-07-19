from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# solution #1
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#
#         res = []
#         for num in arr:
#             if arr.count(num) == 1:
#                 res.append(num)
#         res_list = None
#         for num in res[::-1]:
#             res_list = ListNode(val=num,next=res_list)
#         return res_list
#

# solution #2
class Solution:
    def deleteDuplicates(self, head):
        new_head = ListNode(val=-1, next=head)
        right, left = head, new_head
        while right:
            while right.next and right.val == right.next.val:
                right = right.next

            if left.next == right:
                left = left.next
                right = right.next
            else:
                left.next = right.next
                right = left.next

        return new_head.next


li = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=4, next=ListNode(val=5)))))))
result = Solution().deleteDuplicates(li)
while result:
    print(result.val)
    result = result.next
