# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        n_list = None
        for nums in lists:
            while nums:
                res.append(nums.val)
                nums = nums.next
        res.sort()
        print(res)
        for num in res[::-1]:
            n_list = ListNode(val=num, next=n_list)
        return n_list


l1 = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=5, next=None)))
l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
l3 = ListNode(val=2, next=ListNode(val=6, next=None))
list = [l1, l2, l3]
result = Solution().mergeKLists(list)
while result:
    print(result.val, end='')
    result = result.next
