# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        if n % 2 == 1:
            return False

        pairs = {")": "(", "]": "[", "}": "{"}

        '''
        c là ngoặc mở: đưa vào stack.
        c là ngoặc đóng:
            Kiểm tra stack có rỗng không (rỗng thì sai ngay).
            Lấy ra phần tử ở đỉnh stack.
            So sánh phần tử đó với pairs[c]. Khác nhau thì sai, giống nhau thì đi tiếp
        '''
        for i in range(n):
            if (s[i] in pairs):
                if stack == []:
                    return False
                if pairs[s[i]] != stack.pop():
                    return False
            else:
                stack.append(s[i])
        return stack == []


sol = Solution()
print(sol.isValid("(("))
