class Solution(object):
    def intersect(self, nums1, nums2):
        ret = []
        nums1.sort()
        nums2.sort()
        for num in nums2:
            if num in nums1:
                ret.append(num)
                nums1.remove(num)
        return ret


n1 = [4, 9, 5]
n2 = [9, 4, 9, 8, 4]
result = Solution().intersect(n1, n2)
print(result)
