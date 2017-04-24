class Solution(object):
    lowIndex = 0
    maxLen = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i + 1)
        return s[self.lowIndex: self.lowIndex + self.maxLen]

    def extendPalindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j = j - 1
            k = k + 1
        if self.maxLen < k - j - 1:
            self.maxLen = k - j - 1
            self.lowIndex = j + 1


print(Solution().longestPalindrome('abb'))  # bb
print(Solution().longestPalindrome('cbbd'))  # bb
print(Solution().longestPalindrome('radar'))  # radar
print(Solution().longestPalindrome(
    'babaddtattarrattatddetartrateedredividerb'))  # ddtattarrattatdd
