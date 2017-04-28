class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if str is None:
            return 0
        str = str.strip()
        if len(str) == 0:
            return 0
        positive = False if str[0] == '-' else True
        startIndex = 0
        if str[0] == '+' or str[0] == '-':
            startIndex = 1
        elif str[0].isdigit():
            startIndex = 0
        y = 0
        for i in range(startIndex, len(str)):
            try:
                y = int(str[i]) + y* 10
                if positive and y > MAX_INT:
                    return MAX_INT
                if not positive and -y < MIN_INT:
                    return MIN_INT
            except ValueError:
                return y if positive else -y
        return y if positive else -y



print(Solution().myAtoi(''))
print(Solution().myAtoi('-2147483649'))
print(Solution().myAtoi('-2147483648'))
print(Solution().myAtoi('2147483648'))
print(Solution().myAtoi('2147483647'))
print(Solution().myAtoi('+123'))
print(Solution().myAtoi('-123'))
print(Solution().myAtoi('     %123   '))
print(Solution().myAtoi('     %123 ,,,  '))
print(Solution().myAtoi('     -123,,,  '))