# https://leetcode.com/problems/palindrome-number/

# so am => false
# 0 => true
# ket thuc bang 0 => false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        if x % 10 == 0:
            return False

        x = str(x)
        reversed_x = x[::-1]

        if x == reversed_x:
            return True

        return False


soluton = Solution()
print(soluton.isPalindrome(0))
