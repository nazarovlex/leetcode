nums = [2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                answer = [i, j]
                return answer


print(two_sum(nums, target))
