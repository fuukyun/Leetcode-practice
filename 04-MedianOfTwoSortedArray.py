# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:

    # sol 1
    # def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    #     nums = sorted(nums1 + nums2)
    #     if len(nums) % 2 == 1:
    #         return float(nums[len(nums) // 2])
    #     else:
    #         s1 = len(nums) // 2 - 1
    #         s2 = len(nums) // 2
    #         return (nums[s1] + nums[s2]) / 2

    # sol 2
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        t = m + n
        prev = 0
        curr = 0
        i = 0
        j = 0

        for _ in range(t // 2 + 1):
            prev = curr
            x = nums1[i] if i < m else float('inf')
            y = nums2[j] if j < n else float('inf')

            curr = min(x, y)
            if x == curr:
                i = i + 1
            else:
                j = j + 1

        if t % 2 == 0:
            return (curr + prev) / 2
        else:
            return float(curr)


sol = Solution()
print(sol.findMedianSortedArrays([1, 3, 5], [2, 4]))
