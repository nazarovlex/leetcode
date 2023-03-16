class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # # solution #1 it's work but leet code don't like it
        # if n==0:
        #     return nums1
        #
        # for i in range(m):
        #     print(nums1)
        #     if nums1[i]>nums2[0]:
        #         nums1 = nums1[:-1]
        #         nums1.insert(i,nums2[0])
        #         nums2 = nums2[1:]
        #     elif nums1[i]==nums2[0]:
        #         nums1 = nums1[:-1]
        #         nums1.insert(i, nums2[0])
        #         nums2 = nums2[1:]
        #
        # if len(nums2)>0:
        #     nums1 = nums1[:len(nums1)-len(nums2)]+nums2
        #
        # return nums1

        # # solution #2
        a, b, write_index = m - 1, n - 1, m + n - 1

        while b >= 0:
            print(nums1)
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1
        return nums1


num1 = [1, 2, 3, 0, 0, 0]
m = 3
num2 = [2, 5, 6]
n = 3

number = 2147395599
result = Solution().merge(num1, m, num2, n)
print(result)
