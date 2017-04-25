
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483647 #sys.maxsize
        MIN_INT = -2147483648
        if x > MAX_INT or x < MIN_INT:
            raise Exception('Input number overflow')
        y = 0
        positive = True if x >= 0 else False
        x = abs(x)
        while x != 0:
            y = y * 10 + x % 10
            x = x // 10
            if (-y < MIN_INT and not positive) or (y > MAX_INT and positive):
                return 0
        return y if positive else -y

print(Solution().reverse(1234)) # 4321
print(Solution().reverse(-1234)) # -4321
print(Solution().reverse(0)) # 0
print(Solution().reverse(1147483647)) # 0
print(Solution().reverse(-1147483647)) # 0