class Solution:
    def longestPalindrome(self, s: str) -> str:
        melhor = [-1,'']
        len_s = len(s)
        for i in range(len_s):
            for j in range(i,len_s,1):
                sub_string = s[i:j+1:]
                len_sub = len(sub_string)
                if len_sub > melhor[0]:
                    if sub_string == (sub_string)[::-1]:
                        melhor=[len_sub,sub_string]
                else:
                    pass
        return melhor[1]
