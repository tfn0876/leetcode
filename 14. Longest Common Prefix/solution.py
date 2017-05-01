import operator,functools

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        resultList, j, temp = [], 0, ''
   
        if len(strs) == 0:
            return ""
        while True:
            temp = ''
            for i in range(len(strs)):
                if j >= len(strs[i]):
                    return ''.join(resultList)
                if temp == '':
                    temp = strs[i][j]
                if not strs[i][j] == temp:
                    return ''.join(resultList)
            resultList.append(temp)
            j += 1
        return  ''.join(resultList)

print(Solution().longestCommonPrefix(["a", "aa"]))
print(Solution().longestCommonPrefix(["aca", "cba"]))
print(Solution().longestCommonPrefix(["c", "abc", "abcd"]))
print(Solution().longestCommonPrefix(["ab", "abd", "abcd"]))
print(Solution().longestCommonPrefix([]))
