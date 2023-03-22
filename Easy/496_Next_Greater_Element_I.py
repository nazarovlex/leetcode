from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            if nums2[nums2.index(nums1[i])] < max(nums2[nums2.index(nums1[i]):]):
                for num in nums2[nums2.index(nums1[i]):]:
                    if num > nums1[i]:
                        nums1[i] = num
                        break
            else:
                nums1[i] = -1
        return nums1


n1 = [4, 1, 2]
n2 = [1, 3, 4, 2]

result = Solution().nextGreaterElement(n1, n2)
print(result)
