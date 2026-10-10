# https://leetcode.com/problems/longest-common-prefix/

'''
so sanh theo tung cot
f l o w e r
f l o w
f l i g h t
0 1 2 ...

Cột 0: cả ba đều là f → giữ.
Cột 1: cả ba đều là l → giữ.
Cột 2: o, o, i → khác nhau → dừng.
'''


class Solution():
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)

        # tim do dai cua str ngan nhat trong list
        lengths = []
        for s in strs:
            lengths.append(len(s))

        min_length = min(lengths)
        result = ""

        # lap cot
        for j in range(min_length):
            char = strs[0][j]

            # lap tung chuoi trong cot
            for i in range(n):
                if strs[i][j] != char:
                    return result
            result += char

        return result


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
