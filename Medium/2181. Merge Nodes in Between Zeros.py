from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution #1
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         head_arr = []
#         while head:
#             head_arr.append(head.val)
#             head = head.next
#         tmp = 0
#         res = []
#         for num in head_arr:
#             if num != 0:
#                 tmp += num
#             else:
#                 if tmp == 0:
#                     continue
#                 res.append(tmp)
#                 tmp = 0
#         if tmp>0:
#             res.append(tmp)
#         head = None
#         for num in res[::-1]:
#             head = ListNode(val=num, next=head)
#         return head

# solution #2
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0)
        tmp = 0
        pntr = new_head
        while head:
            if head.val != 0:
                tmp += head.val
            else:
                if tmp == 0:
                    head = head.next
                    continue
                pntr.next = ListNode(tmp)
                pntr = pntr.next
                tmp = 0

            head = head.next
        if tmp > 0:
            pntr.val = tmp
        return new_head.next


li = ListNode(val=0, next=ListNode(val=3, next=ListNode(val=1, next=ListNode(val=0, next=ListNode(val=4,next=ListNode(val=5, next=ListNode(val=2, next=ListNode(val=0))))))))
result = Solution().mergeNodes(li)
while result:
    print(result.val, end=' ')
    result = result.next
