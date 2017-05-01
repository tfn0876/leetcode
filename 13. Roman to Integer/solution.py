class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        RomeDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        result = 0
        last = 0
        for i in range(len(s)):
            cur = RomeDict[s[i]]
            if i > 0 and cur > last:
                result += cur - last - last
            else:
                result += cur
            last = cur
        return result

print(Solution().romanToInt("VI")) # 6
print(Solution().romanToInt("IV")) # 4
print(Solution().romanToInt("XC")) # 90
print(Solution().romanToInt("MMMIM")) # 3999
print(Solution().romanToInt("DCXXI")) # 621