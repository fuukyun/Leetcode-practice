# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows        # numRows ô chứa, mỗi ô độc lập   
        row = 0                      # hàng hiện tại
        step = 1                     # +1: đi xuống, -1: đi lên
        for c in s:
            rows[row] += c              # đưa c vào hàng row
            if row == numRows - 1:      # nếu chạm biên thì đổi hướng
                step = -1
            elif row == 0:
                step = 1
            row += step

        return "".join(rows)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
