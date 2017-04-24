class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        if len(s) <= 1:
            return len(s)
        startIndex = 0
        maxlen = 0
        for i in range(1, len(s)):           
            findIndex = s[startIndex: i].find(s[i])
            if findIndex >= 0:
                startIndex = startIndex + findIndex + 1
            maxlen = max(i - startIndex + 1, maxlen)                   
        return maxlen 


# 3
print(Solution().lengthOfLongestSubstring('abcabcbb'))

# 1
print(Solution().lengthOfLongestSubstring('bbbbb'))

# 3
print(Solution().lengthOfLongestSubstring('pwwkew'))

# 2
print(Solution().lengthOfLongestSubstring('aab'))

# 3
print(Solution().lengthOfLongestSubstring('dvdf'))

# 1
print(Solution().lengthOfLongestSubstring('c'))