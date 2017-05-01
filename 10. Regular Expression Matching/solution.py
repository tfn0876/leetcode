class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.Shrink(p)
        st = [False] * (len(s)+1)
        st[0] = True   
        i = 0
        while i < len(p):
            if i+1 < len(p) and p[i+1] == '*':
                state = st[0]
                for j in range(len(s)):
                    state = st[j+1] or (state and (p[i] == s[j] or p[i] == '.'))
                    st[j+1] = state
                i += 2
                # print(st)
            else:
                for j in range(len(s)-1,-1,-1):
                    st[j+1] = st[j] and (p[i] == s[j] or p[i] == '.')
                st[0] = False
                # print(st)
                i += 1
        return st[-1]

    def Shrink(self, p):
            s = ""
            if len(p) > 4:
                for i in range(len(p)):
                    if p[i] == "*":
                        if len(s) >= 3 and s[len(s) - 2] == "*" and s[len(s) - 1] == s[len(s) - 3]:
                            s = s[0: len(s) - 1]
                        else:
                            s = s + "*" 
                    else:
                        s = s + p[i]
                return s
            else:
                return p      
# print(Solution().isMatch("aa", "a")) # False
# print(Solution().isMatch("aa", "aa")) # True
# print(Solution().isMatch("aaa", "aa")) # False
# print(Solution().isMatch("aa", "a*")) # True
# print(Solution().isMatch("aa", ".*")) # True
# print(Solution().isMatch("ab", ".*")) # True
print(Solution().isMatch("abc", "a*abc*c")) # True
# print(Solution().isMatch("ab", ".*c")) # False
# print(Solution().isMatch("aaa", "ab*a")) # False
# print(Solution().isMatch("a", "ab*")) # True
# print(Solution().isMatch("bbbba", ".*a*a")) # True
# print(Solution().isMatch("a", "a.")) # False
# print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")) # False