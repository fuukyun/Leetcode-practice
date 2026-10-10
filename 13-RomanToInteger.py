# https://leetcode.com/problems/roman-to-integer/

# XII => 12
# IX => 9
# neu x[i] < x[i+1] => cong, nguoc lai tru

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        n = len(s)
        result = 0

        for i in range(n):
            if i + 1 >= n:
                result += roman[s[i]]
                return result
            if (roman[s[i]] >= roman[s[i+1]]):
                result += roman[s[i]]
            else:
                result -= roman[s[i]]


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
