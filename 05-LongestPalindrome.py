# https://leetcode.com/problems/longest-palindromic-substring/

'''
1 ký tự => trả về đúng ký tự đó
palindrome => đọc xuôi hay ngược đều giống nhau
phân biệt hoa thường: "Aa" ko đối xứng

Ý tưởng
- Hướng 1: vét cạn
    + duyệt mọi đoạn con s[i:j]
    + với mỗi đoạn, kiểm tra đối xứng (dùng s[::-1])
    + giữ lại đoạn dài nhất
- Hướng 2: 
    + quan sát: Mọi palindrome đều đối xứng quanh tâm
         r a c e c a r        tâm là 'e' (độ dài lẻ)
         a b b a              tâm nằm giữa hai chữ 'b' (độ dài chẵn)
         Thay vì thử mọi đoạn rồi kiểm tra, 
         ta làm ngược lại: chọn tâm trước, 
         rồi mở rộng ra hai bên chừng nào còn đối xứng.
    + cách làm:
        * từ 1 tâm, đặt 2 con trỏ left, right
        * nếu s[left] == s[right] => đúng, mở rộng thêm left trái, right phải
        * nếu s[left] != s[right] hoặc left < 0, right >= n dừng
        * đoạn dài nhất từ tâm là phần nằm giữa hai con trỏ sau khi dừng
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Sol 1
        # n = len(s)
        # s_result = ""
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         sub = s[i:j]
        #         if (sub == sub[::-1]) and (len(sub) >= len(s_result)):
        #             s_result = sub

        # return s_result

        # sol 2
        n = len(s)

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # Lúc dừng, left và right đang đứng ở vị trí đã vi phạm,
            # nên đoạn palindrome thật sự là s[left + 1 : right]
            return s[left+1:right]

        best = ""
        for i in range(len(s)):
            odd = expand(i, i)      # tâm lẻ: một ký tự
            even = expand(i, i+1)   # tâm chẵn: giữa hai ký tự kề nhau
            print("odd: ", odd, "    ", "even: ", even)
            best = max(best, odd, even, key=len)
        return best


sol = Solution()
print(sol.longestPalindrome("aba"))
