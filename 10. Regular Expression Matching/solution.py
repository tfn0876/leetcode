class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatchShrinked(s, self.Shrink(p))

    def isMatchShrinked(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) > 0 and len(p) == 0:
            return False
        elif len(s) == 0 and len(p) > 0:
            if(len(p) > 1) and p[1] == "*":
                return self.isMatchShrinked(s, p[2: len(p)])
            else:
                return False
        elif len(p) > 1 and p[1] == "*" and (p[0] == "." or s[0] == p[0]):
            return self.isMatchShrinked(s[1: len(s)], p[2: len(p)]) or self.isMatchShrinked(s[1: len(s)], p) or self.isMatchShrinked(s, p[2: len(p)])       
        elif len(p) > 1 and p[1] == "*":
            return self.isMatchShrinked(s, p[2: len(p)])
        else:
            return (p[0] == "." or s[0] == p[0]) and self.isMatchShrinked(s[1: len(s)], p[1: len(p)])

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
        
print(Solution().isMatch("aa", "a")) # False
print(Solution().isMatch("aa", "aa")) # True
print(Solution().isMatch("aaa", "aa")) # False
print(Solution().isMatch("aa", "a*")) # True
print(Solution().isMatch("aa", ".*")) # True
print(Solution().isMatch("ab", ".*")) # True
print(Solution().isMatch("aab", "c*a*b")) # True
print(Solution().isMatch("ab", ".*c")) # False
print(Solution().isMatch("aaa", "ab*a")) # False
print(Solution().isMatch("a", "ab*")) # True
print(Solution().isMatch("bbbba", ".*a*a")) # True
print(Solution().isMatch("a", "a.")) # False
print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")) # False
# print(Solution().Shink("a*a*a*a*a*a*a*a*a*a*c"))