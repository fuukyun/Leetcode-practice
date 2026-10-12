# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# solution 1
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         best = 0
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 sub = s[i:j]
#                 if len(sub) == len(set(sub)):
#                     best = max(best, len(sub))
#         return best

# solution 2

'''
best = 0
left = 0
window = tập rỗng

với mỗi c trong s:
    khi c còn trong window:
        bỏ s[left] khỏi window
        tăng left
    thêm c vào window
    best = max(best, độ dài cửa sổ)

trả về best
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        left = 0
        window = set()

        for c in s:
            while c in window:
                window.remove(s[left])
                left = left + 1

            window.add(c)
            best = max(best, len(window))
        return best


sol = Solution()
print(sol.lengthOfLongestSubstring("ecdffbffcfaafdeeaabadabaaebafdeffcbafeefebdbdbbedcdcdbcfdceddebaefcdeeabfccafccbbacfcbccafbeedcdecacdebadabcfceedbcfddfbfedbeedbcccecbeabeedefdfccfadaacaaedaccdbafedbbebdadedafdcfbcbeeaaccbfaedeaffbdfddaffafaddadbccfcfddeabbcabeeaabaeacaabebbeecbbaffbdcfbdecdfcaeefbadabafccfdbdfbcdcddfbebadbdbdacbcadcecdfaccbaefcfeabacffaccddabbcdffedacdfbaedeaacedaabaeebdcadcabdaffefecebabfeaafebffcaeeaaeaacafecfcfbdadcbadcfdabbfdfeadcedcaefafceeefcaeebdfcbebdbbbababfdebdecaefaafeafbbaffbabdfceaceadfbabcaadabdcceeddfecbcadcfaacccececfabcedebefdfecaffdcdccbebbebeeeadcecebabddbccfcdecccdeddcfbdebcdfbdbbacdfbacfbcbfcbdbafececcbbdedcafbeffbadfcebbeaebbcbdfabbbcdfcacefbdbdbefcdcabafeefdcddaeaedfdadcffedbfaebfcacfafabaecebdbddacdededcccefcedfabcbaeaceafedeeaaffffadcbabbddbecceadebbdecbbebebdbbdeadacedecbfaacefadaabdfdafdabededeaaaccaafbebafcdfaaacbadafbbdefafdccbcafbfbfdbabcbbdfdfbfcbacaacdcadffee"))
