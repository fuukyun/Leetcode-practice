# https://leetcode.com/problems/two-sum/

# soluton 1


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)+1):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# print(twoSum(nums, target))

# solution 2
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}

        for i, num in enumerate(nums):
            com = target - num

            if com in d:
                return [d[com], i]

            d[num] = i

        return []


solution = Solution()

nums = [2, 7, 11, 15]

target = 13

result = solution.twoSum(nums, target)
print(result)
