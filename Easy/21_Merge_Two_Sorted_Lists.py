from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # Solution with arrays
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2, l3 = [], [], []
        while list1:
            l1.append(list1.val)
            list1 = list1.next
        while list2:
            l2.append(list2.val)
            list2 = list2.next
        l3 = l1 + l2
        l3 = sorted(l3, reverse=True)

        list_node = None
        for i in l3:
            list_node = ListNode(val=i, next=list_node)

        return list_node

class Solution2: # Solution without arrays
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = res = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next

        if list1:
            res.next = list1
        elif list2:
            res.next = list2

        return merged.next


list1 = ListNode(val=1, next=ListNode(val=5, next=ListNode(val=7, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=6, next=None)))

s = Solution()
ret = s.mergeTwoLists(list1=list1, list2=list2)

while ret:
    print(ret.val)
    ret = ret.next
