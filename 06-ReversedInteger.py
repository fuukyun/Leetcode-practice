# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        # sol 1: đổi sang chuỗi
        s = str(abs(x))
        s = s[::-1]
        y = int(s)
        z = int(y*(x/abs(x)))

        if -(2**31) <= z <= 2**31 - 1:
            return z
        else:
            return 0


sol = Solution()
print(sol.reverse(0))
