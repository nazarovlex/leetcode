class Solution(object):
    def hasCycle(self, head):
        left = head
        right = head

        while right and right.next:
            left = left.next
            right = right.next.next
            if left == right:
                return True

        else:
            return False