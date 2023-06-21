from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_num, num_2 = 0, 0
        while l1:
            res_num = res_num * 10 + l1.val
            l1 = l1.next

        while l2:
            num_2 = num_2 * 10 + l2.val
            l2 = l2.next

        res_num += num_2

        res_list = None

        while True:
            res_list = ListNode(val=res_num % 10, next=res_list)
            res_num //= 10
            if res_num == 0:
                break

        return res_list


l1 = ListNode(val=7, next=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
result = Solution().addTwoNumbers(l1, l2)
print(result)
