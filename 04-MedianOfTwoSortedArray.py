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
    '''
    # Ý tưởng:
    # - Hai mảng đã sắp xếp sẵn, nên không cần gộp rồi sort lại (như hướng 1).
    # - Dùng hai con trỏ i, j (cho nums1, nums2). Mỗi bước lấy phần tử nhỏ hơn
    #   giữa nums1[i] và nums2[j], rồi dịch con trỏ của mảng vừa bị lấy.
    # - Không cần trộn hết, chỉ cần đi tới vị trí giữa của mảng gộp.
    #
    # Gợi ý:
    # - Phần tử giữa nằm ở chỉ số t // 2 (t = m + n), nên cần lấy t // 2 + 1 phần tử.
    # - Tổng chẵn thì cần hai phần tử giữa, nên phải nhớ giá trị của bước trước.
    # - Một mảng có thể hết trước (hoặc rỗng từ đầu): xử lý sao để không bị
    #   IndexError và không chọn lại phần tử cũ?
    '''
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
